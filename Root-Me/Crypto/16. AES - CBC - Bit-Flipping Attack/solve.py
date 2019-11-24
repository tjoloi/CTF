import base64, string, socket, itertools

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def flip(plain, encrypted, payload, idx):
	plain_bytes = plain[idx:idx+5]
	crypted_bytes = encrypted[idx-16:idx-11]

	block_cipher_out = xor_everything(plain_bytes, crypted_bytes)
	new_cipher = xor_everything(block_cipher_out, payload)

	flipped = encrypted[:idx-16] + new_cipher + encrypted[idx-16+len(new_cipher):]
	return flipped


alphabet = list(string.printable)
alphabet.remove(';')
alphabet.remove('=')
alphabet = ''.join(alphabet)

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge01.root-me.org", 51035))
txt = s.recv(20000)
txt = s.recv(20000)


s.send(b'1\n')
print(s.recv(20000))











plain = (
		b'[id=546815648;na'+
		b'me=AAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b'AAAAAAAAAAAAAAAA'+
		b';is_member=false'+
		b';mail=;pad=0000]')

enc = b'IRZjBh6GxjeYI7YZvxwfBBVkIGD5GOwhVU/65TH5zmHK32CxTby8qrfqOQMck5eZgaNkiS12uSIhWwUl2C9Bxy3/dOB5Y2uTHWeKUPgH3KFRaVpBF6JaTdntiDYsRxhhP6JCHjRSPr7hRtOwBPFdXjB/wt6MR0z2BlP6CUtctfCHziH75WA3T59qBuacvoZSwKXQp7vlsLSpd7WUGChn0ttYbX58+osSLxSi4EXF92Y='
decoded = base64.b64decode(enc)

print(plain)

idx = 64 + 64 + 32 + 59
payload = b'true;'

flipped = flip(plain, decoded, payload, idx)
print(base64.b64encode(flipped))