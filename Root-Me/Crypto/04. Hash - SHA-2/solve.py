import hashlib
encrypted = '96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92'

for i in range(64):
	print(encrypted[:i] + encrypted[i+1:])

# Coller les 64 hashs différents dans https://md5decrypt.net/Sha256/#answer

ans = '4dM1n'.encode()
h = hashlib.sha1(ans)
print(h.hexdigest())
