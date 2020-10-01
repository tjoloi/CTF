import string
from itertools import *

cipher = "JKPF-GZTREQVNXMDSLHCFSMIGMR"

def vigenere(words, key, alphabet=string.ascii_lowercase, case_sensitive=False):
	plain = ''
	idx_key = 0

	if not case_sensitive:
		words = words.lower()

	for c in words:
		if c in alphabet:
			k_idx = alphabet.find(key[idx_key])
			c_idx = alphabet.find(c)
			p_idx = (c_idx - k_idx) % len(alphabet)

			plain += alphabet[p_idx]
			idx_key = (idx_key + 1) % len(key)
		else:
			plain += c
	return plain

for key in product(string.ascii_uppercase, repeat=4):
	if vigenere(cipher[:4], key, string.ascii_uppercase, True) == "FLAG":
		print("Got key:", ''.join(key))
		print("Flag:", vigenere(cipher, key, string.ascii_uppercase, True))
		break