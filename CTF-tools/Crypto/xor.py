def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def get_encrypting_key(key, data_length):
	encrypting_key = b''
	while len(encrypting_key) < len(data_length):
		encrypting_key += key
	encrypting_key = encrypting_key[:data_length]
	return encrypting_key