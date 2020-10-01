from nclib import netcat
from Crypto.Hash import SHA1

nc = netcat.Netcat(('challenges.unitedctf.ca', 4002))


h = nc.recv().decode()

while not 'flag-' in h:
	for i in range(100000):
		sha = SHA1.new(str(i).encode())
		dig = sha.hexdigest()
		if dig == h[:-1]:
			nc.send(str(i))
			break

	h = nc.recv().decode()

print(h)