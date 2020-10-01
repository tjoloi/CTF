from binascii import *
from base64 import *

flag = unhexlify("464c4147") + b64decode("LTQ5NGM2Zjc2NjU0NDYxNw==") + b64encode("461466f72".encode()) + hexlify("6174730a".encode())
print(flag.decode())