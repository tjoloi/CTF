data = None
with open('flag.mid', 'rb') as f:
	header = f.read(4)
	length = f.read(4)
	form = f.read(2)
	tracks = f.read(2)
	divs = f.read(2)
	magic1 = f.read(4)
	t_length = int.from_bytes(f.read(4), 'big')
	data = f.read(t_length)

for i in range(0, len(data), 2):
	print(data[i:i+2])