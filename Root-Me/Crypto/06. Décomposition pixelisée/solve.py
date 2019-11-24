from PIL import Image

lines = []
with open('code.txt', 'r') as f:
	lines = f.readlines()

everything = []
for l in lines:
	p_line = []
	l = l.replace('\n', '')
	pixels = l.split('+')

	for p in pixels:
		v, n = p.split('x')
		for i in range(int(n)):
			everything.append(int(v))

im = Image.new('1', (100, 12))
im.putdata(everything[:-1])
im.show()