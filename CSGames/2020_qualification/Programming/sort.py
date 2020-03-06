import socket

def sort_send(sock, nums):
	arrayed = nums.replace(b' ', b'').split(b',')
	parsed = [int(n) for n in arrayed]
	
	# L'algo se sort est juste là. I know, c'est BS, mais python a quand même
	# un bon algo de sort sooooooooooooooo
	# Btw, Google me dit que c'est une complexité de N log(N)
	# Mais ça a l'air wack vu que ça utilise des algos différents
	# en fonction de je ne sais quoi.
	sort = sorted(parsed)

	ans = ', '.join(map(str, sort))
	ans += '\n'

	sock.send(ans.encode())
	string = sock.recv(20000)
	return string


s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(("csgames-quals.frigon.app", 8100))
string = s.recv(20000)

for i in range(1000):
	split = string.split(b'\n')
	nums = split[-2]
	try:
		string = sort_send(s, nums)
	except ValueError:
		print(f'Got it!\n{split[1].decode()}')
		break
