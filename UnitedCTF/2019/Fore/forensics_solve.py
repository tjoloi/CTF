import re

lines= None
with open('requests.log', 'r') as f:
	lines = f.readlines()

string = ''
octet = ''
for line in lines:
	num = re.search('\\?q=.', line)[0][-1]
	octet += num
	if not len(octet) % 8:
		string += chr(int(octet, 2))
		octet = ''
block_size = len(string)//10
for i in range(10):
	print(string[block_size*i:block_size*(i+1)])
