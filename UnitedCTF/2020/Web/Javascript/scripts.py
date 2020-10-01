# flag = '\x46\x4c\x41\x47\x2d\x65\x37\x65\x62\x66\x62\x62\x39\x64\x63\x66\x35\x63\x66\x62\x36\x30\x61\x65\x31\x62\x62\x35\x39\x64\x34\x30\x66\x37\x36\x39\x35'
# print(flag)

# email = '\x61\x64\x6d\x69\x6e\x40\x6c\x6f\x63\x61\x6c'
# password = '\x50\x40\x61\x73\x73\x77\x30\x72\x64\x21'

# print(email, password)

import xor

charset = 'FLAG-1234567890abcdef'

def reverseFuzz(n):
	n = int(n)
	if n % 2:
		return n - 3
	else:
		return n + 1

flag = "71:74:67:78:43:56:96:2:105:7:53:105:50:56:98:51:98:83:48:97:55:54:56:65:105:104:50:83:61:89:52:65:101:65:54:113:62:3".split(':')
flag = bytearray(map(reverseFuzz, flag))
key1 = b'\x02\x07\x01\x08\x05\x08\x07\x0a\x03\x0f'
key2 = b'2718587a3f'

key1 = xor.get_encrypting_key(key1, len(flag))
key2 = xor.get_encrypting_key(key2, len(flag))

flag1 = xor.xor_everything(flag, key1)
flag2 = xor.xor_everything(flag, key2)

real_flag = ''
for idx, c in enumerate(flag1):
	c = chr(c)
	if c in charset:
		c2 = chr(flag2[idx])
		if c2 in charset:
			print('Colliding:', c, c2)
		real_flag += c
	else:
		real_flag += chr(flag2[idx])

print(real_flag)
