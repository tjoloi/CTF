import string
length = 49

def caesar(word, shift, alphabet=string.ascii_lowercase):
	decoded = ''
	for c in word:
		if c in alphabet:
			decoded += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
		else:
			decoded += c
	return decoded

def shift_once(b):
	return b >> 1

# Ascii value entre 0x61 et 0x7a -> lettres minuscules only
# Fait un rot13 sur les chars minuscules

string = "flag-" + 'abcd' * 11

# flAg-abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd

data = bytes.fromhex('e6f268e85a6ed0be66cc6ebe6eca60c6bee060f4c6666e68c26ebec660d0cabe666eca66be68d0bed0c262ce66e2e06ee6')
data = map(shift_once, data)
rotted_flag = ''
for b in data:
	rotted_flag += chr(b)

print(caesar(rotted_flag, 13))