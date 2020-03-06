import socket, re

# La complexité est toujours de N peu importe pour l'algorithme, though
# On fait quand même un search dans un set à chaque itération qui lui-même
# à une complexité de 1 en moyenne et N dans le pire des cas (ou N est la
# longueur du set dans ce cas là)
def palindrome(sock, mot):
	found = set()

	for c in mot:
		if c in found:
			found.remove(c)
		else:
			found.add(c)

	if len(found) <= 1:
		ans = 'True\n'
	else:
		ans = 'False\n'
		

	sock.send(ans.encode())
	string = sock.recv(20000)
	return string

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(("csgames-quals.frigon.app", 8101))

string = s.recv(20000)
split = string.split(b'\n')

for i in range(1000):
	split = string.split(b'\n')
	mot = split[-2]	
	string = palindrome(s, mot)
	flag = re.findall('flag{.+}', string.decode())
	if flag:
		print(f'Got it!\n{flag[0]}')
		break