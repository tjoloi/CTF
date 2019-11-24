def convert(text, i):
	ret = b''
	for b in text:
		n = b+i
		try: 
			ret += (n).to_bytes(1, 'big')
		except:
			ret += (n-255).to_bytes(1, 'big')
	return ret

txt = ''
with open('ch7.bin', 'rb') as f:
	txt = f.read()

minimum = 9999
for i in range(255):
	converted = convert(txt, i)
	
	# When python converts a byte to a string, it prints b' then will
	# try printing every byte as ascii if it can, else it will print
	# \xNN where NN is the hex value of the byte. The shortest message
	# is the one that has the most ascii values, so it's the most likely
	# to be the right message.
	if len(str(converted)) < minimum:
		minimum = len(str(converted))
		print(converted)


