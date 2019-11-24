from requests import *
import re

def pretty_ans(i, answer):
	return('{"id":"'+i+'","response":"'+answer+'"}')

url = 'https://mrrobot.unitedctf.ca'
s = Session()
resp = s.get('{}/start'.format(url))
text = resp.text[1:-1]
split = re.split(':|,', text)

i = split[1][1:-1]
q = split[-1][1:-1]
print(q)
a1 = 'elliot alderson'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a1))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a2 = 'e corp'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a2))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a3 = 'fsociety'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a3))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a4 = 'eps2.2_init_1.asec'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a4))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a5 = 'allsafe'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a5))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a6 = 'angela moss'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a6))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a7 = 'dark army'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a7))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a8 = 'tyrell wellick'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a8))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a9 = 'morphine'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a9))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)
a10 = 'the careful massacre of the bourgeoisie'

resp = s.post('{}/respond'.format(url), data=pretty_ans(i, a10))
text = resp.text[1:-1]
split = text.split(':')
q =  split[1][1:-1]
print(q)

