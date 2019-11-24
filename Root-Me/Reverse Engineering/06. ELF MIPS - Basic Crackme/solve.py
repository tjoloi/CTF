# s8 + 24 = idx
# S8 + 28 = code[0]
idx = 7
code = list('_'*19)
while idx < 17:
	code[idx+1] = chr(105)
	idx += 1
code[18] = chr(115)
code[17] = chr(112)
code[7] = chr(109)
code[2] = chr(110)
code[6] = chr(110)
code[0] = chr(99)
code[1] = chr(97)
code[3] = chr(116)
code[4] = chr(114)
code[5] = chr(117)

print(''.join(code))