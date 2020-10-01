def h(i: bytes, j: bytes) -> bytes:
	k = list(range(256))
	l = 0
	m = []

	for n in range(256):
		l = (l + k[n] + j[n % len(j)]) % 256
		k[n], k[l] = k[l], k[n]

	n = l = 0
	for o in i:
		n = (n + 1) % 256
		l = (l + k[n]) % 256
		k[n], k[l] = k[l], k[n]
		m.append(o ^ k[(k[n] + k[l]) % 256])

	return m