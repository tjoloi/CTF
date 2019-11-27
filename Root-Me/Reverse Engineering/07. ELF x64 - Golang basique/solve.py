def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def get_encrypting_key(key, data_length):
	encrypting_key = b''
	while len(encrypting_key) < data_length:
		encrypting_key += key
	encrypting_key = encrypting_key[:data_length]
	return encrypting_key

key = b'rootme'
passwd = b'\x3B\x02\x23\x1B\x1B\x0C\x1C\x08\x28\x1B\x21\x04\x1C\x0B'

real_key = get_encrypting_key(key, len(passwd))

print(xor_everything(passwd, real_key))