import collections
import itertools

# c_to_v_mapping = dict(zip(ALPH, itertools.count(0)))
# v_to_c_mapping = {v: k for k, v in c_to_v_mapping.items()}

# cc_to_v_mapping = dict(zip(map(lambda x: "".join(x), itertools.product(ALPH, repeat=2)), itertools.count(0)))
# v_to_cc_mapping = {v: k for k, v in cc_to_v_mapping.items()}

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
	'Vigenere_r1':{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	'Vigenere_r5':{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.32 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 30 }, 
				1000:  { 'k_empt': 20 },
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
				100:   { 'k_empt': 75 },
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
				100:   { 'k_empt': 150 },
				1000:  { 'k_empt': 70 },
				10000: { 'k_empt': 40 },
			}
		}
	},
	'Vigenere_r10':{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	'affine_subst_mono':{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"affine_subst_bi":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"affine_subst_bi":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"uniform_mono":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"uniform_bi":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"g_mono":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
	"g_bi":{
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
				10:	   { 'k_H': 2.8 },
				100:   { 'k_H': 1.3 },
				1000:  { 'k_H': 0.33 }, # for pure |t-p|=0.3, for uni |t-p|=0.25
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
				100:   { 'k_empt': 40 }, 
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
	},
}

# add a_prh_size param to 1_X criterias
for dist_method, crits in criterias_and_params.items():
	for crit, l_cases in crits.items():
		if 'criteria1_' in crit:
			for l_case, L_cases in A_prh_sizes.items():
				for L, params in L_cases.items():
					criterias_and_params[dist_method][crit][l_case][L]['a_prh_size'] = A_prh_sizes[l_case][L]
					#print("smth")

struct_crit_params = {
	10:	   { 'diff_limit': 2.55  }, # does it have sense ?
	100:   { 'diff_limit': 0.615 }, # does it have sense ?
	1000:  { 'diff_limit': 0.34  },
	10000: { 'diff_limit': 0.3   },
}