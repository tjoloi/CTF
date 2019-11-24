def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def get_encrypting_key(key, data_length):
	encrypting_key = b''
	while len(encrypting_key) < data_length:
		encrypting_key += key
	encrypting_key = encrypting_key[:data_length]
	return encrypting_key

str1 = (b'\x89\xAC\x73\xA3\x6C\x04'+
		b'\xA5\xE1\x3E\x95\x47\x12'+
		b'\x96\xBE\x61\xBF\x74\x28'+
		b'\x9B\x95\x71\xB8\x79\x03'+
		b'\x89\xB8\x70\xB2\x76\x02'+
		b'\xA5\xA5\x61\x89\x7D\x01'+
		b'\x9B\xA2\x4A\xA3\x77\x0E'+
		b'\xA5\xAF\x67\xB3\x50')
str1 = str1[::-1]
str2 = b'\x77\xFA\xCA\x15\xD6\x18'
str2 = str2[::-1]

key = get_encrypting_key(str2, len(str1))
out = xor_everything(str1, key)

print(out)