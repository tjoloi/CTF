def parse_conv(lines):
	table = {}
	for line in lines:
		data = line.split(' ')
		add_entry(table, data[0], data[1], float(data[2]))
		add_entry(table, data[1], data[0], 1/float(data[2]))
	return table

def add_entry(d, src, dst, val):
	if not src in d:
		d[src] = {}
	d[src][dst] = val

def evaluate(src, dst):
	path.append(src)
	if dst in conversion_table[src]:
		return conversion_table[src][dst]
	else:
		for conv in conversion_table[src].keys():
			if not conv in path:
				src_p = conv
				ret = conversion_table[src][src_p]*evaluate(src_p, dst)
				if not ret == 0: return ret
	return 0


global conversion_table
global path
with open('conversions.txt', 'r') as f:
	lines = f.readlines()
	conversion_table = parse_conv(lines)

evals = []
with open('aConvertir.txt', 'r') as f:
	evals = f.readlines()

total = 0
for e in evals:
	path = []
	q, src, dst = e.split(' ')
	dst = dst.replace('\n', '')
	q = int(q)
	temp = q*evaluate(src, dst)
	total += temp
	print(f'{q} {src} is worth {temp} {dst}')
print(f"{'-'*50}\nEverything is worth {total}")