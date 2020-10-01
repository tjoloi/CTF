from binascii import hexlify, unhexlify
from xor import xor_everything

def ctr_same_key_nonce(encrypted_flag=0, encrypted_oracle=0, plaintext_oracle=0, help=False):
	if print_help:
		print('''\
Attack on AES CTR reusing the same secret key and nonce.
To sucessfully decrypt the flag, we need 2 important parts.

First is obviously the encrypted flag. Second is an oracle encrypted from known plaintext. 
This function supports 2 data formats, the first being hex encoded data in a plain string
	and the second is a byte array of raw data.

Internally it works this way
Let's pose these variables:
	k  := Encryption block(s) generated by the aes functions
	m1 := Flag
	c1 := Encrypted Flag
	m2 := Our oracle
	c2 := Our oracle encrypted

Our goal is to get m1

We know that
	c1 = k ^ m1
	c2 = k ^ m2

Using basic math on the xor operator, we can pose this equality
	c1 ^ c2 = (k ^ m1) ^ (k ^ m2) = m1 ^ m2 ^ k ^ k = m1 ^ m2

Which gives us the flag
	m1 = c1 ^ c2 ^ m2\
			''')
		return
	
	enc_flag = b''
	enc_oracle = b''
	plain_oracle = b''
	
	# Handling both hex strings and byte arrays
	try:
		enc_flag = unhexlify(encrypted_flag)
		enc_oracle = unhexlify(encrypted_oracle)
		plain_oracle = unhexlify(plaintext_oracle)
	except:
		enc_flag = encrypted_flag
		enc_oracle = encrypted_oracle
		plain_oracle = plaintext_oracle

	M1xM2 = xor_everything(enc_flag, enc_oracle)
	return xor_everything(M1xM2, plaintext_oracle),encode()