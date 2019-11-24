import json, bz2
global old_rand

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def get_encrypting_key(key, data_length):
	encrypting_key = b''
	while len(encrypting_key) < data_length:
		encrypting_key += key
	encrypting_key = encrypting_key[:data_length]
	return encrypting_key

keys = []
code = b''
with open('rainbowall.key', 'rb') as f:
	keys = f.read().split(b'\x00')[:-1]
with open('oDjbNkIoLpaMo.bz2.crypt', 'rb') as f:
	code = f.read()

answer = b''
index = 0
for key in keys:
	if not index % 100000:
		print(f'{index} out of {len(keys)}')

	k = get_encrypting_key(key, len(code))
	data = xor_everything(k, code)
	index += 1
	try:
		answer = bz2.decompress(data)
		break
	except:
		pass

answer = answer.replace(b'\xe9', b'e')
print(answer.decode())