from nclib import netcat
from binascii import hexlify, unhexlify
from Crypto.Util.Padding import pad

charset = b'0123456789abcdef'

def sendPayloadAndReturnEnc(payload):
	nc.send('2\n')
	nc.recv()
	nc.send(hexlify(payload) + b'\n')
	recv = nc.recv()
	split = recv.split(b'\n')
	# print(split[0].decode())
	return unhexlify(split[0].split(b' ')[1])

nc = netcat.Netcat(('challenges.unitedctf.ca', 3003))
# nc = netcat.Netcat(('localhost', 6969))
nc.recv()
encFlag = sendPayloadAndReturnEnc(b'')
nbBlocksRef = len(encFlag) // 16

nbBlocks = nbBlocksRef
padder = b''
while nbBlocks == nbBlocksRef:
	padder += b'\x00'
	nbBlocks = len(sendPayloadAndReturnEnc(padder)) / 16

padder = padder + b'\x00'
# padder = b'000000'
flagLength = (nbBlocksRef * 16) - (len(padder) - 1) - len('FLAG-')
flag = b''

while len(flag) < flagLength:
	for c in charset:
		tmpFlag = chr(c).encode() + flag
		payload = pad(tmpFlag, 16) + padder

		pad(payload + b'FLAG-' + b'*' * flagLength, 16)

		enc = sendPayloadAndReturnEnc(payload)
		# print(enc[-16:])
		# print(enc[:16])
		# print('-'*30)
		blocksDone = len(tmpFlag) // 16

		substr = enc[-((blocksDone+1)*16):-(blocksDone*16)] if blocksDone else enc[-16:]
		if substr == enc[:16]:
			flag = chr(c).encode() + flag
			padder += b'\x00'
			padder = padder[:len(padder) % 16]
			break

	print('Current known flag:', flag)
print('FLAG-' + flag.decode())
