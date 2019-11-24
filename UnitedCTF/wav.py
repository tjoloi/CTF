def bytes2hex(bs):
	arr = []
	for b in bs:
		arr.append(hex(b))
	return arr

def bytes2chr(bs):
	arr = []
	for b in bs:
		arr.append(chr(b))
	return ''.join(arr)

def bytes2int(bs):
	value = 0
	for i in range(len(bs)):
		b = bs[i]
		value += b*(256**i)
	return value

def read_block(bs):
	b1 = bs.pop(0)
	b2 = bs.pop(0)
	return bytes2int([b1, b2])

def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask


bs = None

with open('message_cropped.wav', 'rb') as f:
	bs = list(f.read())

FileTypeBlocID = bytes2chr(bs[0:4])
FileSize = bytes2int(bs[4:8])
FileFormatID = bytes2chr(bs[8:12])

FormatBlocID = bytes2chr(bs[12:16])
BlocSize = bytes2int(bs[16:20])
AudioFormat = bytes2int(bs[20:22])
NbrCanaux = bytes2int(bs[22:24])
Frequence = bytes2int(bs[24:28])
BytePerSec = bytes2int(bs[28:32])
BytePerBloc = bytes2int(bs[32:34])
BitsPerSample = bytes2int(bs[34:36])

DataBlocID = bytes2chr(bs[36:40])
DataSize = bytes2int(bs[40:44])


metadata = [FileTypeBlocID, FileSize, FileFormatID, FormatBlocID,
				BlocSize, AudioFormat, NbrCanaux, Frequence, BytePerSec,
				BytePerBloc, BitsPerSample, DataBlocID, DataSize]
print('Constante: {}'.format(metadata[0]))
print('Taille totale: {}'.format(metadata[1] + 8))
print('Format fichier: {}\n'.format(metadata[2]))
print('Format bloc: {}'.format(metadata[3]))
print('Taille bloc: {}'.format(metadata[4]))
print('Format audio: {}'.format(metadata[5]))
print('Nombre canaux: {}'.format(metadata[6]))
print('Fréquence échantillonage: {}'.format(metadata[7]))
print('Octets par seconde: {}'.format(metadata[8]))
print('Octets par bloc: {}'.format(metadata[9]))
print('Bits par échantillon: {}\n'.format(metadata[10]))
print('Constante: {}'.format(metadata[11]))
print('Taille data: {}'.format(metadata[12]))

bs = bs[44:]

string = ''
wip = []

while bs:
	raw_byte = read_block(bs)
	byte = getSignedNumber(raw_byte, 16)
	# print(byte, bin(raw_byte))
	

	if byte < -30000:
		print(bin(raw_byte)[-1])
	# if byte > 100:
	# 	print('1')
	# elif byte < -100:
	# 	print('0')

print(string)