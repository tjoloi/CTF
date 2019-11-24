# Input ^ key = secret
# Good input = key ^ secret

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])


key = b'=\xC9\xAE\xEB\xB0\xB6\x7F\xD2\x36\xD1\x86\xCF\xAA\x8E\xC9\x14\x73\xB9\x02\x62\x3C\x18\x74\x23'
secret = b'\x4D\xB9\xC6\x87\xD8\xC6\x0F\xBA\x5A\xB9\xF6\xBF\xC2\xE2\xA1\x64\x03\xD1\x6E\x0A\x4C\x68\x1C\x4F'

answer = xor_everything(key, secret)
print(answer)

# Ma réponse marche pas, mais j'ai remarqué que ça avait l'air de se 
# répéter pas mal so j'ai essayé juste pphlh comme mot de passe
# pis c'était good. 