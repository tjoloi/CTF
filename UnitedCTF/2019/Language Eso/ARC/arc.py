def execute(line, stack):
	cmd, arg = line.split('.')
	arg = arg[1:-1]

	if cmd == 'I':
		stack.append(stack.pop() + stack.pop())
	elif cmd == 'II':
		stack.append(stack.pop() - stack.pop())
	elif cmd == 'III':
		stack.append(stack.pop() * stack.pop())
	elif cmd == 'IV':
		stack.append(stack.pop() // stack.pop())
	elif cmd == 'V':
		stack.append(stack.pop() & stack.pop())
	elif cmd == 'VI':
		stack.append(stack.pop() | stack.pop())
	elif cmd == 'XX':
		print(' '.join(str(c) for c in reversed(stack)))
	elif cmd == 'XXI':
		stack.pop()
	elif cmd == 'XXII':
		stack.append(from_rom(arg))

def from_rom(c):
	if c == 'I':
		return 1
	elif c == 'V':
		return 5
	elif c == 'X':
		return 10
	elif c == 'L':
		return 50
	elif c == 'C':
		return 100
	else:
		raise Exception(f'Unknown roman numeral: {c}')

lines = []

with open('program.arc', 'r') as f:
	lines = f.readlines()

stack = []
for line in lines:
	execute(line, stack)

# I. Ajoute les deux derniers éléments du stack
# II. Soustrait les deux derniers éléments du stack
# III. Multiplie les deux derniers éléments du stack
# IV. Divise les deux derniers éléments du stack
# V. Effectue un ET logique sur les deux derniers éléments du stack
# VI. Effectue un OU logique sur les deux derniers éléments du stack
# VII. à XIX. Aucune instruction.
# XX. Imprime le stack actuel sous forme de chaîne de caractères
# XXI. Enlève le dernier élément.
# XXII. Pousse un nouvel élément dans le stack. L'élément doit être écrit en chiffre romain, mais un élément est inséré à la fois. 