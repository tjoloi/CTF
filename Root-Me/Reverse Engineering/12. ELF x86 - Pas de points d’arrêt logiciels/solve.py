def ROR(x, n, bits = 32):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

def ROL(x, n, bits = 32):
    return ROR(x, bits - n, bits)

def wild_func():
	eax = 0x08048080
	ebx = 0x08048123
	ecx = 0x0

	ebx = ebx-eax
	while ebx > 0:
		ecx += eax & 0xff
		ecx &= 0xff
		ROL(ecx, 3)
		eax += 1
		ebx -= 1
	return ecx

ecx = wild_func()
edx = ecx

barr1 = b'\x1e\xcd\x2a\xd5\x34\x87\xfc\x78\x64\x35\x9d\xec\xde\x15\xac\x97\x99\xaf\x96\xda\x79\x26\x4f'
barr2 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
for idx in range(0x19, 0, -1):
	eax = barr1[idx-1]
	ebx = barr2[idx-1]
	edx = ROR(edx, 1)