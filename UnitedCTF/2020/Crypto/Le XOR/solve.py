import base64

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

def get_encrypting_key(key, data_length):
	encrypting_key = b''
	while len(encrypting_key) < data_length:
		encrypting_key += key
	encrypting_key = encrypting_key[:data_length]
	return encrypting_key

cipher = "ERsWEHoYOQcyIiMWIiQkPhE2ND47MjoyOSMVJSIjMjE4JTQyJQ=="
decoded = base64.b64decode(cipher)

# clear = "FLAG".encode()
# for i in range(4):
# 	print(xor_everything([decoded[i]], [clear[i]]))

key = "W".encode()
flag = xor_everything(decoded, get_encrypting_key(key, len(decoded)))
print(flag)