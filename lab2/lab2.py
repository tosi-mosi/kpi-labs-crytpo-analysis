import re
import itertools
import random
import collections
import math
import functools
import operator

ALPH = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

def nth(iterable, n, default=None):
	return next(itertools.islice(iterable, n, None), default)

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return map(operator.add, a, b)

def format_text(file_name):
	with open(file_name, 'r') as rf:
		lower_cased = rf.read().lower()
		g_untailed = lower_cased.replace('ґ', 'г')
		non_letters_replaced = re.sub(r'[^а-щьюяґєії]', '', g_untailed)
		#print(non_letters_replaced[:200])
		with open('output_file', 'w') as of:
			of.write(non_letters_replaced)

def read_formatted_text(file_name):
	with open(file_name, 'r') as rf:
		return rf.read()

"""
delete this
return {
	'Vigenere': 			[[distorted_text_pieces_L10_N10000:...], [distorted_text_pieces_L100_N10000:...], ...],
	'affine_subst_mono': 	[[distorted_text_pieces_L10_N10000:...], [distorted_text_pieces_L100_N10000:...], ...].
	...
}
delete this
# returns [[text_pieces_L10_N10000:...], [text_pieces_L100_N10000:...], ...]
"""
def distort_text_pieces(method: str, input_texts: list):
	c_to_v_mapping = dict(zip(ALPH, itertools.count(0)))
	v_to_c_mapping = {v: k for k, v in c_to_v_mapping.items()}

	cc_to_v_mapping = dict(zip(map(lambda x: "".join(x), itertools.product(ALPH, repeat=2)), itertools.count(0)))
	v_to_cc_mapping = {v: k for k, v in cc_to_v_mapping.items()}

	def Vigenere(input_text, r):
		result = ''
		key = "".join(random.choices(ALPH, k = r))

		for i in range(len(input_text)):
			result += v_to_c_mapping[(c_to_v_mapping[input_text[i]] + c_to_v_mapping[key[i%r]]) % len(ALPH)]
		return result

	def Vigenere_r1(input_text):
		return Vigenere(input_text, 1)

	def Vigenere_r5(input_text):
		return Vigenere(input_text, 5)

	def Vigenere_r10(input_text):
		return Vigenere(input_text, 10)		

	def affine_subst_mono(input_text):
		result = ''
		a = random.randint(1, len(ALPH)-1)
		b = random.randint(0, len(ALPH)-1)

		for i in range(len(input_text)):
			result += v_to_c_mapping[(a * c_to_v_mapping[input_text[i]] + b) % len(ALPH)]
		return result

	def affine_subst_bi(input_text):
		result = ''
		a = random.randint(1, len(ALPH)**2-1)
		b = random.randint(0, len(ALPH)**2-1)

		for i in range(0, len(input_text), 2):
			bi = input_text[i:i+2]
			if(len(bi) == 2):
				result += v_to_cc_mapping[(a * cc_to_v_mapping[input_text[i:i+2]] + b) % len(ALPH)**2]
		return result

	def uniform_mono(input_text):
		return "".join([v_to_c_mapping[round(random.uniform(0, len(ALPH)-1))] for i in range(len(input_text))])

	def uniform_bi(input_text):
		return "".join([v_to_cc_mapping[round(random.uniform(0, len(ALPH)**2-1))] for i in range(0, len(input_text), 2)])

	def g_mono(input_text):
		y0 = random.randint(1, len(ALPH)-1)
		y1 = random.randint(0, len(ALPH)-1)
		y = [y0, y1]

		for i in range(2, len(input_text)):
			y.append((y[-1]+y[-2])%len(ALPH))

		return "".join(map(lambda x: v_to_c_mapping[x], y))

	def g_bi(input_text):
		y0 = random.randint(1, len(ALPH)**2-1)
		y1 = random.randint(0, len(ALPH)**2-1)
		y = [y0, y1]

		for i in range(4, len(input_text), 2):
			y.append((y[-1]+y[-2])%len(ALPH)**2)

		return "".join(map(lambda x: v_to_cc_mapping[x], y))

	# result = []
	#result = {method:text_piece_group for text_piece_group in map(locals()[method], input_texts)}
	# result = list(zip(input_texts, map(locals()[method], input_texts)))
	result = list(map(locals()[method], input_texts))

	return result

# returns [[text_pieces_L10_N10000:...], [text_pieces_L100_N10000:...], ...]
def cut_to_non_overlapping_text_pieces(input_text, piece_length, num_of_pieces) -> list:
	result = []
	for i in range(num_of_pieces):
		cur_offset = i * piece_length
		text_piece = input_text[cur_offset:cur_offset+piece_length]
		if text_piece:
			result.append(text_piece)
		else:
			break
	return result

def calculate_freq(input_text, input_len, mono_case=True):
	freq = collections.defaultdict(int)
	if mono_case:
		for i in range(0, input_len):
			freq[input_text[i]] += 1
	else:
		for i in range(0, input_len):
			if(len(input_text[i:i+2]) == 2):
				freq[input_text[i:i+2]] += 1

	l_gram_iterable = ALPH if mono_case else pairwise(ALPH)
	for i in l_gram_iterable:
		freq[i]
	#print(freq)
	return freq

def calculate_H(freq, input_len, mono_case=True):
	unzero_an_iterable = lambda x: filter(lambda y: y!=0, x)
	if mono_case:
		# H1
		return - sum(map(lambda x:x/input_len * math.log(x/input_len, 2), unzero_an_iterable(freq.values())))
	else:
		# H2
		# should it be input_len - 1?
		return -0.5 * sum(map(lambda x:x/(input_len-1) * math.log(x/(input_len-1), 2), unzero_an_iterable(freq.values())))

def calculate_stats(input_text):
	# mono_freq = collections.defaultdict(int)
	# bi_freq = collections.defaultdict(int)
	# input_len = len(input_text)
	# for i in range(0, input_len):
	# 	mono_freq[input_text[i]] += 1
	# 	if(len(input_text[i:i+2]) == 2):
	# 		bi_freq[input_text[i:i+2]] += 1 	# overlapping bigrams

	input_len = len(input_text)
	mono_freq = calculate_freq(input_text, input_len)
	bi_freq   = calculate_freq(input_text, input_len, mono_case=False)

	# unzero_an_iterable = lambda x: filter(lambda y: y!=0, x)
	# H1 = - sum(map(lambda x:x/input_len * math.log(x/input_len, 2), unzero_an_iterable(mono_freq.values())))
	# H2 = -0.5 * sum(map(lambda x:x/(input_len-1) * math.log(x/(input_len-1), 2), unzero_an_iterable(bi_freq.values())))		# should it be input_len - 1?
	H1 = calculate_H(mono_freq, input_len)
	H2 = calculate_H(bi_freq, input_len, mono_case=False)	
	print(f'H1={H1}, H2={H2}')

	# I1 = sum(map(lambda x:x*(x-1), mono_freq.values())) / ((input_len) * (input_len - 1))
	# I2 = sum(map(lambda x:x*(x-1), bi_freq.values())) / ((input_len) * (input_len - 1))

	# for i in ALPH:
	# 	mono_freq[i]
	# for i in itertools.product(ALPH, repeat=2):
	# 	bi_freq[i]
	return (mono_freq, bi_freq, H1, H2)



def check_criterias(text_pieces, mono_freq, bi_freq, H1, H2, sentient_ukr_text=False):

	# maybe different A_prh lengths for different Ls ?
	A_prh_sizes = {
		'mono_case': {
			10:    3,
			100:   3,
			1000:  3,
			10000: 3,
		},
		'bi_case': {
			10:    10,
			100:   10,
			1000:  8,
			10000: 8,
		}
	}

	criteria5_0_js = {
		'mono_case': {
			'j1': 3,
			'j2': 5,
			'j3': 7,
		},
		'bi_case': {
			'j1': 50,
			'j2': 100,
			'j3': 200,
		}
	}

	nested_default_dict = lambda: collections.defaultdict(nested_default_dict)
	criterias_and_params = {
		'criteria1_0': nested_default_dict(),
		'criteria1_1': {
			'mono_case': {
				10:    { 'k_p': 5 },
				100:   { 'k_p': 2 },
				1000:  { 'k_p': 1 },
				10000: { 'k_p': 1 },
			},
			'bi_case': {
				10:	   { 'k_p': 15 },
				100:   { 'k_p': 10 },
				1000:  { 'k_p': 5 },
				10000: { 'k_p': 5 },
			}
		},
		'criteria1_2': nested_default_dict(),
		'criteria1_3': nested_default_dict(),
		'criteria3_0': {
			'mono_case': {
				10:	   { 'k_H': 2 },
				100:   { 'k_H': 1.5 },
				1000:  { 'k_H': 1.2 },
				10000: { 'k_H': 0.6 },
			},
			'bi_case': {
				10:	   { 'k_H': 1 },
				100:   { 'k_H': 0.8 },
				1000:  { 'k_H': 0.7 },
				10000: { 'k_H': 0.6 },
			}
		},
		'criteria5_1_j1': {
			'mono_case': {
				10:	   { 'k_empt': 2 },
				100:   { 'k_empt': 2 },
				1000:  { 'k_empt': 2 },
				10000: { 'k_empt': 2 },
			},
			'bi_case': {
				10:	   { 'k_empt': 45 }, # 50 ящ, и 10 бигр. Если все бигр будут разн -> 40 пустіх
				100:   { 'k_empt': 35 }, 
				1000:  { 'k_empt': 25 },
				10000: { 'k_empt': 15 },
			}
		},
		'criteria5_1_j2': {
			'mono_case': {
				10:	   { 'k_empt': 2 },
				100:   { 'k_empt': 2 },
				1000:  { 'k_empt': 2 },
				10000: { 'k_empt': 2 },
			},
			'bi_case': {
				10:	   { 'k_empt': 95 }, # 100 ящ, и 10 бигр
				100:   { 'k_empt': 70 },
				1000:  { 'k_empt': 60 },
				10000: { 'k_empt': 30 },
			}
		},
		'criteria5_1_j3': {
			'mono_case': {
				10:	   { 'k_empt': 2 },
				100:   { 'k_empt': 2 },
				1000:  { 'k_empt': 2 },
				10000: { 'k_empt': 2 },
			},
			'bi_case': {
				10:	   { 'k_empt': 195 },
				100:   { 'k_empt': 160 },
				1000:  { 'k_empt': 70 },
				10000: { 'k_empt': 40 },
			}
		}
	}

	# add a_prh_size param to 1_X criterias
	for crit, l_cases in criterias_and_params.items():
		if 'criteria1_' in crit:
			for l_case, L_cases in A_prh_sizes.items():
				for L, params in L_cases.items():
					criterias_and_params[crit][l_case][L]['a_prh_size'] = A_prh_sizes[l_case][L]
					# params['a_prh_size'] = A_prh_sizes[l_case][L]

	#print(criterias_and_params)

	def criteria1_0(input_text, mono_case=True, a_prh_size=None):
		a_prh = sorted_freq_mono[:a_prh_size] if mono_case else sorted_freq_bi[:a_prh_size]
		#print(a_prh)
		for prh_l_gram in a_prh:
			if prh_l_gram in input_text:
				return False
		return True

	def criteria1_1(input_text, mono_case=True, k_p=None, a_prh_size=None):
		a_prh = sorted_freq_mono[:a_prh_size] if mono_case else sorted_freq_bi[:a_prh_size]
		prh_encountered = 0
		for prh_l_gram in a_prh:
			if prh_l_gram in input_text:
				prh_encountered += 1
			if prh_encountered >= k_p:
				return False
		return True

	def criteria1_2(input_text, mono_case=True, a_prh_size=None):
		#print((mono_freq, sorted_freq_mono) if mono_case else (bi_freq, sorted_freq_bi))
		theor_freq, a_prh = (mono_freq, sorted_freq_mono[:a_prh_size]) if mono_case else (bi_freq, sorted_freq_bi[:a_prh_size])
		pract_freq = collections.defaultdict(int)
		l_gram_iterable = input_text if mono_case else pairwise(input_text)
		for l_gram in l_gram_iterable:
			pract_freq[l_gram] += 1
			if pract_freq[l_gram] >= theor_freq[l_gram]:
				return False
		return True

	def criteria1_3(input_text, mono_case=True, a_prh_size=None):
		theor_freq, a_prh = (mono_freq, sorted_freq_mono[:a_prh_size]) if mono_case else (bi_freq, sorted_freq_bi[:a_prh_size])
		pract_freq = collections.defaultdict(int)
		l_gram_iterable = input_text if mono_case else pairwise(input_text)
		for l_gram in l_gram_iterable:
			pract_freq[l_gram] += 1

		if sum(pract_freq.values()) >= sum(theor_freq[k] for k in pract_freq):
			return False
		return True

	def criteria3_0(input_text, mono_case=True, k_H=None):
		theor_freq, theor_H = (mono_freq, H1) if mono_case else (bi_freq, H2)
		pract_freq = collections.defaultdict(int)
		l_gram_iterable = input_text if mono_case else pairwise(input_text)
		for l_gram in l_gram_iterable:
			pract_freq[l_gram] += 1

		pract_H = calculate_H(pract_freq, len(input_text), mono_case=mono_case)
		#print(theor_H, pract_H)
		if abs(theor_H - pract_H) > k_H:
			return False
		return True

	def criteria5_0(input_text, mono_case=True, j=None, k_empt=None):
		B_frq = sorted_freq_mono[-j:] if mono_case else sorted_freq_bi[-j:]
		pract_freq = collections.defaultdict(int)
		l_gram_iterable = input_text if mono_case else pairwise(input_text)
		for l_gram in l_gram_iterable:
			if l_gram in B_frq:
				pract_freq[l_gram] += 1

		if len(list(filter(lambda x: pract_freq[x]==0, B_frq))) >= k_empt:
			return False
		return True

	def criteria5_1_j1(input_text, mono_case=True, k_empt=None):
		j = criteria5_0_js['mono_case']['j1'] if mono_case else criteria5_0_js['bi_case']['j2']
		return criteria5_0(input_text, mono_case=mono_case, j=j, k_empt=k_empt)

	def criteria5_1_j2(input_text, mono_case=True, k_empt=None):
		j = criteria5_0_js['mono_case']['j2'] if mono_case else criteria5_0_js['bi_case']['j2']
		return criteria5_0(input_text, mono_case=mono_case, j=j, k_empt=k_empt)

	def criteria5_1_j3(input_text, mono_case=True, k_empt=None):
		j = criteria5_0_js['mono_case']['j3'] if mono_case else criteria5_0_js['bi_case']['j3']
		return criteria5_0(input_text, mono_case=mono_case, j=j, k_empt=k_empt)


	# # crit_1_1 params
	# k_p = 20

	sorted_freq_mono = sorted(mono_freq, key=mono_freq.get)
	sorted_freq_bi = sorted(bi_freq, key=bi_freq.get)

	for text_piece_group in text_pieces:
		L = len(text_piece_group[0])
		print(f'  crits for text group with L = {L}, N = {len(text_piece_group)}')

		if not sentient_ukr_text:
			print(f'    {"":<15} {"f_n_mono":<15} {"f_n_bi":<15}')
		else:
			print(f'    {"":<15} {"f_p_mono":<15} {"f_p_bi":<15}')
		for crit_name, crit_params in criterias_and_params.items():
			crit_results_mono = list(map(functools.partial(locals()[crit_name], **crit_params['mono_case'][L]), text_piece_group))
			crit_results_bi = list(map(functools.partial(locals()[crit_name], **crit_params['bi_case'][L], mono_case=False), text_piece_group))

			if not sentient_ukr_text:
				# calculate false Negative
				f_prob_mono = crit_results_mono.count(True)/len(crit_results_mono)
				f_prob_bi = crit_results_bi.count(True)/len(crit_results_bi)
			else:
				# calculate false Positive
				f_prob_mono = crit_results_mono.count(False)/len(crit_results_mono)
				f_prob_bi = crit_results_bi.count(False)/len(crit_results_bi)

			print(f'    {crit_name:<15} {round(f_prob_mono, 13):<15} {round(f_prob_bi, 13):<15}')
		# filter()
		# for text_piece in text_piece_group:

		# 	criteria1_0_mono_result = criteria1_0(text_piece, A_prh_mono)
		# 	criteria1_0_bi_result = criteria1_0(text_piece, sorted_freq_bi)
		# 	criteria1_1_mono_result = criteria1_1(text_piece, A_prh_mono, k_p)
		# 	criteria1_1_bi_result = criteria1_1(text_piece, sorted_freq_bi, k_p)
		# 	criteria1_2_mono_result = criteria1_2(text_piece, A_prh_mono, mono_freq)
		# 	criteria1_2_bi_result = criteria1_2(text_piece, A_prh_bi, bi_freq, mono_case=False)
		# 	criteria1_3_mono_result = criteria1_3(text_piece, A_prh_mono, mono_freq)
		# 	criteria1_3_bi_result = criteria1_3(text_piece, A_prh_bi, bi_freq, mono_case=False)

if __name__ == '__main__':

	random.seed(1)

	text = read_formatted_text('lab2/formatted_ukr.txt')	
	
	L_and_N = [
		(10,    10000),
		(100,   10000),
		(1000,  10000),
		(10000, 1000)
	]

	# need 10 mill, currently have 1 mill
	# 10 10000
	# 100 10000
	# 1000 1008
	# 10000 101


	text_piece_groups = list(map(lambda x: cut_to_non_overlapping_text_pieces(text, *x), L_and_N))
	#print(f"text_len = {len(text_piece_groups)}, {len(text_piece_groups[0])}, {len(text_piece_groups[1])}")
	for i in text_piece_groups:
		print(len(i[0]), len(i))
	#print(list(map(len, r[3])))
	# print(r)
	
	#print(distort_text_pieces('Vigenere', text_pieces[1]))
	# # print(distort_text_pieces('affine_subst_mono', text_pieces[0]))
	# print(distort_text_pieces('uniform_bi', text_pieces[0]))
	# print(distort_text_pieces('g_bi', text_pieces[0]))



	# mono_freq, bi_freq, H1, H2 = calculate_stats(text)

	# h_p_mono = 2 # у великому тексті усі букви зустрінуться !
	# h_p_bi = 15
	# A_prh_mono = sorted(mono_freq, key=mono_freq.get)[h_p_mono]
	# A_prh_bi = sorted(bi_freq, key=bi_freq.get)[h_p_bi]

	# print(len(sorted({v:k for k,v in mono_freq.items()}.items())))
	# print(sorted({v:k for k,v in bi_freq.items()}.items()))


	# criteria1_0(text_pieces[0][0], A_prh_mono)
	# criteria1_0(text_pieces[0][0], A_prh_bi)

	stats = calculate_stats(text)

	distortion_methods = [
		'Vigenere_r1',
		'Vigenere_r5',
		'Vigenere_r10',
		'affine_subst_mono',
		'affine_subst_bi',
		'uniform_mono',
		'uniform_bi',
		'g_mono',
		'g_bi',
	]

	# for distorted
	for distortion_method in distortion_methods:
		print(f'checking criteria for {distortion_method} distortion method')
		distorted_text_piece_groups = []
		for text_piece_group in text_piece_groups:
			distorted_text_piece_groups.append(distort_text_pieces(distortion_method, text_piece_group))
		check_criterias(distorted_text_piece_groups, *stats)

	# for pure ukr literature
	print(f'checking criteria for pure ukraining text')
	check_criterias(text_piece_groups, *stats, sentient_ukr_text=True)