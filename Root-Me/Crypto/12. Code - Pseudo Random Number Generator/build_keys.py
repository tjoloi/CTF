import string
global old_rand

def srand(seed):
	global old_rand
	old_rand = seed

def rand():
	global old_rand
	old_rand = old_rand * 214013 + 2531011
	old_rand &= 0xffffffff
	temp = old_rand >> 16
	return temp & 0x7fff

def gen_key(length = 32):
	alphabet = string.ascii_letters + '123456789'
	key = ''
	for i in range(length):
		key += alphabet[rand() % len(alphabet)]
	key += '\x00'
	return key

seen = {}
deltas = []
offset = 1354320000
end = 1356998399 + 1
keys = ''
with open('rainbowall.key', 'wb') as f :
	for i in range(offset, end):
		srand(i)
		key = gen_key()

		# if key.startswith('aM5'):
		# 	print(key, f'\n{i-offset} out of {end-offset}')
		f.write(key.encode())
		if not i % 100000:
			print(f'{i-offset} out of {end-offset}')
		
