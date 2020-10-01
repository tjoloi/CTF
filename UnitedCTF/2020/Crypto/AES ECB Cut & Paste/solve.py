from Crypto.Util.Padding import pad, unpad
from nclib import netcat

# General explanation
# We'll try to isolate the remaining "False" into it's own block so that we can replace it with our encrypted "true" block
# To get an encrypted "true" block, we need to use the pad function from Crypto (using the same lib is a safe bet)

# Our payload will consist of 4 blocks
# B1: Pad with 0s to isolate "name=" -> name=(0*11)
# B2: pad('True'.encode(), 16)
# B3: Pad with 0s to isolate "&flag=" -> (0*10)&flag=
# B4: the remaining "False"
#
# Then we send to server E1+E3+E2

padded = pad('True'.encode(), 16)
payload = b'0'*11 + padded + b'0'*10 + b'\n'


nc = netcat.Netcat(('challenges.unitedctf.ca', 3002))
nc.recv()
nc.send('1\n')
nc.recv()
nc.send(payload)
recv = nc.recv().split(b'\n')
data = recv[1].split(b' ')[1]

E1 = data[0:32]
E2 = data[32:64]
E3 = data[64:96]

nc.send('2\n')
nc.recv()

key = E1+E3+E2+b'\n'

nc.send(key)

print(nc.recv().split(b'\n')[0].decode())