from requests import *
import re

resp = get('https://spider.unitedctf.ca')

print(resp.text)
