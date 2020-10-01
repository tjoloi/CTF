from nclib import netcat

nc = netcat.Netcat(('challenges.unitedctf.ca', 4001))
eq = nc.recv()

while not b'flag-' in eq:
	nc.send(str(eval(eq)))
	eq = nc.recv()

print(eq.decode())