import string

def caesar(word, shift, alphabet=string.ascii_lowercase):
	decoded = ''
	for c in word:
		try:
			decoded += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
		except:
			decoded += c
	return decoded

for i in range(26):
	dec = caesar("IODJ-YHQLYLGLYLFL", i, string.ascii_uppercase)
	if 'FLAG-' in dec:
		print(dec, '\nWith n =', i)
		break