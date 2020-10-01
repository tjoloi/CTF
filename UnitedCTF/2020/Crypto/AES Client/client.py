from Crypto.Cipher import AES
from nclib import netcat
from binascii import unhexlify
import json
import sys

nc = netcat.Netcat(('challenges.unitedctf.ca', 3000))
loaded = json.loads(nc.recv())

while not 'flag' in loaded:
	cipher = None
	key = unhexlify(loaded['key'])
	if loaded['mode'] == 'ECB':
		cipher = AES.new(key, AES.MODE_ECB)

	elif loaded['mode'] == 'CBC':
		cipher = AES.new(key, AES.MODE_CBC, iv=unhexlify(loaded['iv_or_counter']))

	elif loaded['mode'] == 'CTR':
		cb0 = unhexlify(loaded['iv_or_counter'])
		cipher = AES.new(key, AES.MODE_CTR, nonce=cb0[:8], initial_value=cb0[8:])
	else:
		print('Unknown AES mode:', loaded['mode'])
		sys.exit()

	if loaded['operation'] == 'encrypt':
		enc = cipher.encrypt(loaded['data'].encode()).hex()
		nc.send(enc)
	else:
		data = unhexlify(loaded['data'])
		dec = cipher.decrypt(data)
		nc.send(dec)

	nc.recv(), '\n' + '*'*30
	loaded = json.loads(nc.recv())

print('Flag is:', loaded['flag'])
