import string
global alphabet
alphabet = string.ascii_lowercase

def shift_word(w, s):
	decoded = ''
	for c in w:
		decoded += alphabet[(alphabet.index(c) - s) % len(alphabet)]
	return decoded


cipher ="""
			tm bcsv qolfp
			f'dmvd xuhm exl tgak
			hlrkiv sydg hxm
			qiswzzwf qrf oqdueqe
			dpae resd wndo
			liva bu vgtokx sjzk
			hmb rqch fqwbg
			fmmft seront sntsdr pmsecq
		""".replace('	', '')[1:-1].replace("'", ' ')
lines = cipher.split('\n')

shift = 25
decoded = ''
for line in lines:
	words = line.split(' ')
	for w in words:
		decoded += shift_word(w, shift)
		decoded += ' '
		shift -= 1
	decoded += '\n'
decoded = decoded[:-1]

print(decoded+'\n')

passwd = ''
for line in decoded.split('\n'):
	passwd += line[0]
for line in decoded.split('\n'):
	passwd += line[-2]
print(f'Password is {passwd}')