import re

data = None

with open('raresteak.ace', 'rb') as f:
	data = f.read()

# with open('FI.png', 'rb') as f:
# 	data = f.read()

matches = re.findall(b'\x89PNG.+', data, flags=re.S)
image = matches[0]

print(image)

with open('image.png', 'wb') as f:
	f.write(image)