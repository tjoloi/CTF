import json
import jwt

message = {
    "unique_name": "admin",
 	"nbf": 1572627356,
 	"exp": 1573232156,
 	"iat": 1572627356
}

compact_jws = jwt.encode(message, 'secret', algorithm='HS256')
print(compact_jws)
dec = jwt.decode(compact_jws, 'secret', 'HS256')
print(dec)

# FLAG-9e4ef6a1-a6e6-43b3-b83d-e4c67c705b99