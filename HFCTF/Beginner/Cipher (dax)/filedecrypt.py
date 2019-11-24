import re
# out = inp[i] + pwd[i] - (len(pwd) + sum(pwd)%10)
# out + len(pwd) + sum(pwd)%10 - pwd[i] = inp[i]

def sum_str(string):
	ret = 0
	for c in string:
		ret += ord(c)
	return ret

def decrypt(enc, passw):
	decrypted = ''
	s = sum_str(passw) % 10
	l = len(passw)
	i = 0
	for c in enc:
		cd = c + l + s - ord(passw[i % l])
		decrypted += chr(cd)
		i += 1
	return decrypted


file1 = './flag.txt.enc'

data = None
with open(file1, 'rb') as f:
	data = f.read()

passwords = []
with open('rocksmall.txt', 'r') as f:
	passwords = f.read().split('\n')

possibilities = ''
for p in passwords:
	try:
		dec = decrypt(data, p)
		possibilities += dec
		possibilities += '\n'
	except ValueError:
		continue
	except ZeroDivisionError:
		continue

matches = re.findall('You found a flag!.+', possibilities)
if matches:
	print(matches[0])
else:
	print('Found nothing...')