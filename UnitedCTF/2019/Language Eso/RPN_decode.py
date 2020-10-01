def evaluate(sign, n2, n1):
	stg = '{}{}{}'.format(n1, sign, n2)
	return eval(stg)

string = '9 9 * 9 + 9 + 2 + 8 ^ 4 + 5 ^ 4 * 5 2 * + 6 8 * 9 8 * 5 + 5 ^ 2 * 1 + 6 5 + 5 * 5 8 * 6 + 8 ^ 9 + 9 ^ 7 + : 9 5 * 9 ^ 4 ^ + 6 + 9 ^ 4 ^ + 9 ^ 5 ^ + 2 + 9 ^ 4 ^ + 5 +'
string = list(string.replace(' ', ''))
pile = []
ans = ''

while string:
	c = string.pop(0)
	if c == ':':
		print(pile.pop())
	elif c in '*+':
		pile.append(evaluate(c, pile.pop(), pile.pop()))
	elif c == '^':
		pile.append(evaluate('^', pile.pop(), pile.pop()))
	else:
		pile.append(c)

print(pile)


