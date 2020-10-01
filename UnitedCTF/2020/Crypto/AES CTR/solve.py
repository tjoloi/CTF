from nclib import netcat
from binascii import hexlify, unhexlify

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

nc = netcat.Netcat(('challenges.unitedctf.ca', 3001))
nc.recv()
nc.send('1\n')

encFlag = unhexlify(nc.recv().split(b'\n')[0].split(b' ')[1])

nc.send('2\n')
nc.recv()
nc.send('0' * len(encFlag) + '\n')

oracle = unhexlify(nc.recv().split(b'\n')[0].split(b' ')[1])

M1xM2 = xor_everything(encFlag, oracle)
flag = xor_everything(M1xM2, b'0' * len(encFlag))
print(flag.decode())

# k ^ m1 = c1
# k ^ m2 = c2
# c1 ^ c2 = m1 ^ m2 ^ k ^ k => m1 ^ m2