import re
import itertools
import random
import collections
import math

ALPH = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

def nth(iterable, n, default=None):
	return next(itertools.islice(iterable, n, None), default)

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

def distort_text_pieces(method: str, input_texts: list) -> str:
	c_to_v_mapping = dict(zip(ALPH, itertools.count(0)))
	v_to_c_mapping = {v: k for k, v in c_to_v_mapping.items()}

	cc_to_v_mapping = dict(zip(map(lambda x: "".join(x), itertools.product(ALPH, repeat=2)), itertools.count(0)))
	v_to_cc_mapping = {v: k for k, v in cc_to_v_mapping.items()}

	def Vigenere(input_text):
		result = ''

		r = 5
		key = "".join(random.choices(ALPH, k = r))

		for i in range(len(input_text)):
			result += v_to_c_mapping[(c_to_v_mapping[input_text[i]] + c_to_v_mapping[key[i%r]]) % len(ALPH)]
		return result

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
			result += v_to_cc_mapping[(a * cc_to_v_mapping[input_text[i:i+2]] + b) % len(ALPH)**2]
		return result

	def uniform_mono(input_text):
		return [v_to_c_mapping[round(random.uniform(0, len(ALPH)-1))] for i in range(len(input_text))]

	def uniform_bi(input_text):
		return [v_to_cc_mapping[round(random.uniform(0, len(ALPH)**2-1))] for i in range(0, len(input_text), 2)]

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

		for i in range(2, len(input_text), 2):
			y.append((y[-1]+y[-2])%len(ALPH)**2)

		return "".join(map(lambda x: v_to_cc_mapping[x], y))

	result = []
	result = list(map(locals()[method], input_texts))
	#result = list(zip(input_texts, map(locals()[method], input_texts)))

	return result

def cut_to_non_overlapping_text_pieces(input_text, piece_length, num_of_pieces) -> list:
	result = []
	for i in range(num_of_pieces):
		cur_offset = i * piece_length
		text_piece = input_text[cur_offset:cur_offset+piece_length]
		if text_piece:
			result.append(text_piece)
	return result

def calculate_stats(input_text):
	mono_freq = collections.defaultdict(int)
	bi_freq = collections.defaultdict(int)
	input_len = len(input_text)
	for i in range(0, input_len):
		mono_freq[input_text[i]] += 1
		if(len(input_text[i:i+2]) == 2):
			bi_freq[input_text[i:i+2]] += 1 	# overlapping bigrams

	H1 = - sum(map(lambda x:x/input_len * math.log(x/input_len, 2), mono_freq.values()))
	H2 = -0.5 * sum(map(lambda x:x/input_len * math.log(x/input_len, 2), bi_freq.values()))
	# I1 = sum(map(lambda x:x*(x-1), mono_freq.values())) / ((input_len) * (input_len - 1))
	# I2 = sum(map(lambda x:x*(x-1), bi_freq.values())) / ((input_len) * (input_len - 1))

	for i in ALPH:
		mono_freq[i]
	for i in itertools.product(ALPH, repeat=2):
		bi_freq[i]
	return (mono_freq, bi_freq, H1, H2)

def cryterium1_0(input_text):


if __name__ == '__main__':

	random.seed(1)

	text = read_formatted_text('lab2/format_text')
	
	L_and_N = [
		(10,    10000),
		(100,   10000),
		(1000,  10000),
		(10000, 1000)			# maybe need 10 million chars text for this? now have only 1 mill
	]

	text_pieces = list(map(lambda x: cut_to_non_overlapping_text_pieces(text, *x), L_and_N))
	#print(f"text_len = {len(text)}, th's = {len(r[2])}, h of th's = {len(r[3])}")
	#print(list(map(len, r[3])))
	# print(r)
	
	# print(distort_text_pieces('Vigenere', text_pieces[1]))
	# # print(distort_text_pieces('affine_subst_mono', text_pieces[0]))
	# print(distort_text_pieces('uniform_bi', text_pieces[0]))
	# print(distort_text_pieces('g_bi', text_pieces[0]))

	mono_freq, bi_freq, H1, H2 = calculate_stats(text)

	h_p = 5
	A_prh_mono = sorted(mono_freq, key=mono_freq.get)[h_p]
	A_prh_bi = sorted(bi_freq, key=bi_freq.get)[h_p]
	

	cryterium1_0()