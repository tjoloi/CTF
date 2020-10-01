import base64, os, pytesseract, string
from nclib import netcat
from PIL import Image, ImageFilter, ImageOps

def read_img():
	data_length = 0
	received = 0
	img = b''
	data = nc.recv()

	try:
		data_length = int(data.decode())
	except ValueError:
		data_length, img = data.split(b'\n')
		data_length = int(data_length.decode())

	while received < data_length:
		data = nc.recv()
		img += data
		received += len(data)

	return img[:-1]

def apply_racism(img_data, debug=False):
	with open('tmp.png', 'wb') as f:
		f.write(img_data)

	img = Image.open('tmp.png')
	data = img.getdata()

	if not debug:
		os.remove('tmp.png')

	out = []

	for pixel in data:
		out.append(racism(pixel))
	img.putdata(out)
	
	if debug:
		img.save('raced.png')

	return img

def racism(pixel):
	reference = (255, 69, 0)
	return (0, 0, 0) if pixel == reference else (255, 255, 255)

trying = True

while trying:
	nc = netcat.Netcat(('challenges.unitedctf.ca', 4003))
	i = 0

	while i < 10:
		try:
			img_data = base64.b64decode(read_img())
		except:
			break

		img = apply_racism(img_data, True)
		charset = string.ascii_letters + string.digits
		charset = charset.replace('o', '').replace('O', '')
		text = pytesseract.image_to_string(img, config=f'-c tessedit_char_whitelist={charset} --psm 6')
		print(i, text.strip())
		nc.send(text)
		i += 1
	
	if i == 10:
		trying = False
	print('-' * 20)

nc.recv()
print(nc.recv().decode()[:-1])