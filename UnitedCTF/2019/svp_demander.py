import socket

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(("svpdemandergentiment.unitedctf.ca", 42000))

s.recv(20000).decode()
labyrinth = s.recv(20000).decode()

print(labyrinth)
print('Done')