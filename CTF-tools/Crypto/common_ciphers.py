import string

def caesar(word, shift, alphabet=string.ascii_lowercase):
	decoded = ''
	for c in word:
		decoded += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
	return decoded

def vigenere(words, key, alphabet=string.ascii_lowercase, case_sensitive=false):
	plain = ''
	idx_key = 0

	if not case_sensitive:
		words = lower(words)

	for c in words:
		if c in alphabet_L:
			k_idx = alphabet.find(key[idx_key])
			c_idx = alphabet.find(c)
			p_idx = (c_idx - k_idx) % len(alphabet_L)

			plain += alphabet[p_idx]
			idx_key = (idx_key + 1) % len(key)
		else:
			plain += c
	return plain