import json, string, itertools
import jwt

alphabet  = string.printable

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFub255bW91cyJ9.5oZKEQUkX1WmOnQx3hv0uiWQOyXkKo6FWr0DNLeAykw'

message = {
 	"username": "admin",
 	"jti": "e2c663bf-d27c-47c2-beaa-4dbdb85b00fd",
 	"iat": 1572630502,
 	"exp": 1572634102
}

enc = jwt.encode(message, 'secret', algorithm='HS256')
print(enc)

dec = jwt.decode(enc, 'secret', 'HS256')
print(dec)

