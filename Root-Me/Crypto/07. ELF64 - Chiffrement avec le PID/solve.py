from paramiko import client
from passlib.hash import md5_crypt as md5
import re, time

def exec(c, command):
	stdin, stdout, stderr = c.exec_command(command)
	return stdout.read().decode()

def pretty(message):
	return re.sub('\x1b\\[.*?m', '', message)
uname = 'cryptanalyse-ch21'
pword = 'cryptanalyse-ch21'
port = 2221

c = client.SSHClient()
c.set_missing_host_key_policy(client.AutoAddPolicy)
c.connect('challenge01.root-me.org', port=port, username=uname, password=pword)

channel = c.invoke_shell()
print(channel.recv(200000).decode())
for i in range(2):
	print(pretty(channel.recv(65535).decode()))
	print('-'*20)
	time.sleep(1)

channel.send('ps\n')
time.sleep(1)

ps = pretty(channel.recv(65535).decode())

print(ps)
m = re.search('.* ps', ps, flags=re.M)
pid = m[0].split(' ')[0]
pid = f'{int(pid) + 1}'

salt = 'awesome'
h = md5.using(salt=salt).hash(pid.encode())
h = h.replace('$', '\\$')
print(h)

comm = f'./ch21 {h}\n'
channel.send(comm)
print(pretty(channel.recv(65535).decode()))
time.sleep(1)

channel.send('cat ./.passwd\n')
print(pretty(channel.recv(65535).decode()))
time.sleep(1)

channel.send('cat ./.passwd\n')
print(pretty(channel.recv(65535).decode()))
