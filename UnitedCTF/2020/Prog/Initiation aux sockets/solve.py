from nclib import netcat

nc = netcat.Netcat(('challenges.unitedctf.ca', 3004))
r = nc.recv()
nc.send(r)
print(nc.recv().decode())