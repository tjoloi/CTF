data = ''
with open('file (1).3d', 'r') as f:
	data = f.read().split('\n')

flag = ''
for line in data:
	if 'F1350.' in line:
		idx = line.index('F')
		speed = line[idx:]
		c = speed.split('.')[-1]
		c = int(c)

		if c == 0:
			continue
		
		c = chr(c)
		flag += c
print(flag)

