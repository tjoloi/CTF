solved = [57, 73, 79, 16, 18, 26, 74, 50, 13, 38, 13, 79, 86, 86, 87]
solved.reverse()
key = 'I know, you love decrypting Byte Code !'
i = 19
answer = []

for n in solved:
	k = ord(key[i])

	s = (n ^ k) - i
	# s += 255 if s < 0 else 0
	answer.append(s)

	print(i)
	i -= 1

answer.reverse()
print(answer)
print(''.join([chr(e) for e in answer]))
# print(answer.reverse())

# i = 5
# (x + i ^ k) % 255
# i += 1

# s = (ord(n) + I) ^ key[I]
# ord(n) = (s^key[i]) - i

# print((255+19^70)%255)
# print((85+255) ^ 70)