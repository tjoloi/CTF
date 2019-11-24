import struct

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])

file_data = []
with open('ch3.bmp', 'rb') as f:
	file_data = f.read()

# We know thw BMP magic byte and it's length.
# While looking at the raw file data, I saw alot of g`mmdo
# a few times back to back and assumed it was all the same bytes.
# This leads me to think that the key is 6 bytes long.
# That mean that we only need those 2 informations to
# decrypt the file.

key = b''
known = b'\x42\x4D'
known += struct.pack('<I', len(file_data))
l = len(known)

print(known)
key += xor_everything(known, file_data[:l])

print(key)

encrypting_key = b''
while len(encrypting_key) < len(file_data):
	encrypting_key += key
encrypting_key = encrypting_key[:len(file_data)]

decrypted_data = xor_everything(file_data, encrypting_key)
with open('plain.bmp', 'wb') as f:
	f.write(decrypted_data)