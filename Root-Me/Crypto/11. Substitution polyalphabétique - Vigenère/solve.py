import string, itertools
global alphabet_U
global alphabet_L
global dic

# DOES NOT WORD, GO TO DCODE.FR TO GET ANSWER

def vigenere_decrypt(words, key):
	plain = ''
	idx_key = 0
	for c in words:
		if c in alphabet_L:
			k_idx = alphabet_L.find(key[idx_key])
			c_idx = alphabet_L.find(c)
			p_idx = (c_idx - k_idx)
			if p_idx < 0:
				p_idx += 26
			plain += alphabet_L[p_idx]
			idx_key = (idx_key + 1) % len(key)
		else:
			plain += c
	return plain

def get_n_valid_words(text):
	count = 0
	for w in text.replace('\n', ' ').split(' '):
		if  len(w) > 2 and w in dic:
			count += 1
	return count

dic = []
code = ''

with open('dictionaire.txt', 'r', encoding='utf-8') as f:
	dic = f.read().split('\n')[:-1]

with open('code.txt', 'r') as f:
	code = f.read()

# code = ' '.join(code.split(' ')[:100])

alphabet_L = string.ascii_lowercase
alphabet_U = string.ascii_uppercase

best_c = 0
best_k = ''
best = ''
# for l in range(2, 10):
# 	for key in itertools.combinations_with_replacement(alphabet_L, l):
# 		plain = vigenere_decrypt(code, key)
# 		count = get_n_valid_words(plain)	
# 		if count > best_c:
# 			best_c = count
# 			best = plain
# 			best_k = key
# 			print(f'New Best!!!\nText: {best}\nKey: {best_k}\nCount: {best_c}')

key = 'thementor'
print(vigenere_decrypt(code.lower(), key))
