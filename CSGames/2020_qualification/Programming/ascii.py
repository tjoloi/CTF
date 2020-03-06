import socket, re

# Un beau p'tit dict pour hardcode mes chiffres
def art_2_num(lines):
	nums = {
		'###\n# #\n# #\n# #\n###' : 0,
		'  #\n  #\n  #\n  #\n  #' : 1,
		'###\n  #\n###\n#  \n###' : 2,
		'###\n  #\n###\n  #\n###' : 3,
		'# #\n# #\n###\n  #\n  #' : 4,
		'###\n#  \n###\n  #\n###' : 5,
		'###\n#  \n###\n# #\n###' : 6,
		'###\n  #\n  #\n  #\n  #' : 7,
		'###\n# #\n###\n# #\n###' : 8,
		'###\n# #\n###\n  #\n  #' : 9
	}
	return nums[lines]

# Un peu chiant à parse tbh
def parse_convert(sock, nums):
	n = (len(nums[0])-1)//4

	parsed = []
	for i in range(n):
		parsed.append([])

	for line in nums:
		idx = 0
		for i in range(0, len(line)-1, 4):
			num_line = line[i:i+4]
			parsed[idx].append(num_line[1:])
			idx += 1

	ans = ''
	for p in parsed:
		joined = '\n'.join(p)
		ans += str(art_2_num(joined))

	ans += '\n'
	sock.send(ans.encode())
	string = sock.recv(20000).decode()
	return string


s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(("csgames-quals.frigon.app", 8102))

string = s.recv(20000).decode()

for i in range(1000):
	split = string.split('\n')
	mot = split[2:]	
	string = parse_convert(s, mot)
	flag = re.findall('flag{.+}', string)
	if flag:
		print(f'Got it!\n{flag[0]}')
		break
