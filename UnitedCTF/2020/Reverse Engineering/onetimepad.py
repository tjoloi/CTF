def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

part1 = bytearray.fromhex('2623bec687f6ee2e101de3694311ab3881fa928f4370f6f6453a0f323fefcc4ba609b3')
part2 = bytearray.fromhex('5313c7ebe09782482369905d0e70984af3cae5ba7644868476527f4b5cdca82f957bc1')

p1 = b''
p2 = b''
for i in range(0, len(part1), 8):
	p1 += part1[i:i+8][::-1]
	p2 += part2[i:i+8][::-1]


flag = xor_everything(p1, p2).decode()
flag = flag[:-2] + flag[-1:-3:-1]
print(flag)

