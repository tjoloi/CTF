secret = [0x46,0x4D,0x43,0x4A,0x31,0x7C,0x6E,0x3B,0x7C,0x68,0x3E,0x6A,0x79,0x40,0x81,0x82,0xA1]

string = ''
for i in range(len(secret)):
	print(secret[i])
	print(i)
	print(chr(secret[i]-i))
	string += chr(secret[i]-i)

print(string)