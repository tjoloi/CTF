import socket
import requests
from PIL import Image
from time import sleep

class Intersection(object):
	def __init__(self, initPosition):
		self.position = initPosition
		self.characterNum = 0

class Case(object):
	def __init__(self, trulyPassable):
		self.isPassable = trulyPassable
		self.isVisited = False
		
	def visit(self):
		self.isVisited = True
		
	def visited(self):
		return self.isVisited
		
	def passable(self):
		return self.isPassable

	def __repr__(self):
		return '*' if not self.passable() else ' ' 
		
def passable(data,x,y):
	if x < len(data[y]) and x >= 0 and y < len(data) and y >= 0:
		return data[y][x].passable()
	else:
		return False

def visited(data,x,y):
	if x < len(data[y]) and x >= 0 and y < len(data) and y >= 0:
		return data[y][x].visited()
	else:
		return True

# s = socket.socket(
#     socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("ctf.cfiul.ca", 24001))

# s.recv(20000).decode()
# labyrinth = s.recv(20000).decode()

# print(labyrinth)

print('Opening image...')
img = Image.open('map.png')
labyrinth = list(img.getdata())
print('Done\n')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

data = [[]]

start = []
finish = []
currentY = 0;

print('Parsing image to data...')

for c in labyrinth:
	if c == GREEN:
		data[currentY].append(Case(False))
		data.append([])
		currentY += 1
	elif c == RED:
		start.append(len(data[currentY]))
		start.append(currentY)
		data[currentY].append(Case(True))
	elif c == BLUE:
		finish.append(len(data[currentY]))
		finish.append(currentY)
		data[currentY].append(Case(True))
	elif c == BLACK:
		data[currentY].append(Case(False))
	elif c == WHITE:
		data[currentY].append(Case(True))

print('Done\n')

currentPos = start.copy()
path = ""
lastIntersections = [Intersection(start.copy())]
print('Start: {}\nFinish: {}\n'.format(start, finish))


print('Solving...')
loop = 0
while currentPos != finish:
	loop += 1
	x = currentPos[0]
	y = currentPos[1]
	pathNum = passable(data,x - 1,y) + passable(data,x + 1,y) + passable(data,x,y - 1) + passable(data,x,y + 1)
			
	lastIntersection = lastIntersections[-1]
	
	if pathNum >= 3 and lastIntersection.position != currentPos:
		lastIntersection = Intersection(currentPos.copy())
		lastIntersections.append(lastIntersection)		
	
	data[y][x].visit()
	
	if passable(data,x - 1,y) and not visited(data,x - 1,y):
		currentPos[0] -= 1
		path += '"left",'
		lastIntersections[-1].characterNum += 7
		
	elif passable(data,x + 1,y) and not visited(data,x + 1,y):
		currentPos[0] += 1
		path += '"right",'
		lastIntersections[-1].characterNum += 8
		
	elif passable(data,x,y - 1) and not visited(data,x,y - 1):
		currentPos[1] -= 1
		path += '"up",'
		lastIntersections[-1].characterNum += 5
		
	elif passable(data,x,y + 1) and not visited(data,x,y + 1):
		currentPos[1] += 1
		path += '"down",'
		lastIntersections[-1].characterNum += 7

	else:
		if pathNum >= 3:
			lastIntersections.pop()
			
			lastIntersection = lastIntersections[-1]
			path = path[:-lastIntersection.characterNum]
			lastIntersections[-1].characterNum = 0
			currentPos = lastIntersection.position.copy()
		else:
			path = path[:-lastIntersection.characterNum]
			lastIntersections[-1].characterNum = 0
			currentPos = lastIntersection.position.copy()
	if not loop % 100000:
		print('Loop number {}'.format(loop))
		print('Path lenght: {}'.format(len(path)))

print('Done\n')

print('Sending solution...')		
path = '[{}]'.format(path[:-1])

s = requests.Session()
resp = s.post('https://lost.unitedctf.ca/', json=path)
print('	Response: {}'.format(resp.text))
print('Done\n')

print('Exporting solved image...')

export = img.copy()
img.close()

current_p = start
# current_p[1] = 200 - current_p[1]

for move in path[1:-1].split(','):
	move = move[1:-1]
	if move == 'right':
		current_p[0] += 1
	elif move == 'down':
		current_p[1] += 1
	elif move == 'up':
		current_p[1] -= 1
	elif move == 'left':
		current_p[0] -= 1
	else:
		raise Exception('Invalid move: {}'.format(move))

	color = export.getpixel(tuple(current_p))
	if color == WHITE or color == BLUE:
		export.putpixel(current_p, (255, 0, 0))
	else:
		export.putpixel(current_p, (0, 255, 0))

export.save('solved.png')
export.close()
with open('path.txt', 'w') as f:
	print(path, file=f)
print('Done')
# s.send(path.encode())
# print(s.recv(20000))
