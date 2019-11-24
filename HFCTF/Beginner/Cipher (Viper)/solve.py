import base64, string

def caesar(word, shift, alphabet=string.ascii_lowercase):
	decoded = ''
	for c in word:
		decoded += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
	return decoded

b64 = 'SEYtNmQzZTdmMTlhNjhlM2FjOWY4ZGM2ODNhYTJlNjFlZDY='
print(base64.b64decode(b64).decode())

# crypt = 'XV-vvrru3u1627s71rvru5suut8sus9s6q9'
# print(caesar(crypt, 10, alphabet = alph))