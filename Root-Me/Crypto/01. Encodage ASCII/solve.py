code = ''
with open('ch8.txt', 'r') as f:
	code = f.read()

result = ''
while code:
	c = code[:2]
	code = code[2:]
	result += chr(int(c, 16))

print(result)