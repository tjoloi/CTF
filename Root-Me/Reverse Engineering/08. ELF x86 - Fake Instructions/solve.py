# dest = b'_0cGj35m9V5T3\xC3\x878CJ0\xC3\x809H95h3xdh'
# addr = [0 for i in range(30)]
# string = '_Celebration'
# for idx, c in enumerate(string):
# 	addr[idx] = c
# dest = dest[:5] + b'\x63' + dest[6:]
# dest = dest[:0x16] + b'\x00' + dest[0x17:]

# print(dest[:0x16])
# print(addr)

# print(0x17 & 0xFFFFFFC)
# ecx = 20

# for i in range(0, 20, 4):

# string = '_0cGjc5m_.5T3Ç8'

string = ''
string += b'\x5F\x30\x63\x47'.decode('utf-8')
string += b'\x6A\x63\x35\x6D'.decode('utf-8')
string += b'\x5F\x2E\x35\x54'.decode('utf-8')
string += b'\x43\x4A\x30\xC3\x80'.decode('utf-8')
string += b'\x39\x48\x39'.decode('utf-8')

print(string)

# It was "liberté!". Voir le fichier d'IDA pour comprendre.