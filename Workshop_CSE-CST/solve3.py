def shr(dest, count=1):
	return dest >> count

str_input = 'aeiouy.aaaaaaaaaaa yuoieaA'
length = len(str_input)
length_prime = length - 2

if len(str_input) <= 25: print("Bad length")
if not str_input[:6].upper() == 'AEIOUY': print('Bad start')

idx = 0
while idx < length_prime:
	if not str_input[idx] == str_input[length_prime]:
		print('Bad mirror')
		break
	idx += 1
	length_prime -= 1