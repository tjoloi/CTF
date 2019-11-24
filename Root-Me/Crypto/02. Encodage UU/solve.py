from codecs import decode

file = ''
with open('ch1.txt', 'r') as f:
	file = f.read()
print(decode(file.encode(), 'uu').decode()[:-1])