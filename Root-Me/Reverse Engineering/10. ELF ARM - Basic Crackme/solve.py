from z3 import *

password = ""
val = 0

x0, x1, x2, x3, x4, x5 = Reals('x0 x1 x2 x3 x4 x5')

# password[3] = 72
# password[6] = 0

s = Solver()
s.add(x3 == 0x72)
s.add(x0 == x5)
s.add(x1 == (x0 + 1))
s.add(x0 == (x3 + 1))
s.add(x5 == (x2 + 4))
s.add(x2 == (x4 + 2))

print(s.check())
print(s.model())

lst = [115, 116, 111, 114, 109, 115]
for val in lst:
	print(chr(val))

