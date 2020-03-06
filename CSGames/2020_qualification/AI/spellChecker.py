import string
global words

def missing_char(arr, word):
	for i in range(len(word)):
		for c in string.ascii_lowercase:
			word_prime = word[:i] + c + word[i:]
			if word_prime in words:
				arr.add(word_prime)

def added_char(arr, word):
	for i in range(len(word)):
		word_prime = word[:i] + word[i+1:]
		if word_prime in words:
			arr.add(word_prime)

def wrong_char(arr, word):
	for i in range(len(word)):
		for c in string.ascii_lowercase:
			word_prime = word[:i] + c + word[i+1:]
			if word_prime in words:
				arr.add(word_prime)

def swapped_char(arr, word):
	for i in range(len(word)-1):
		b_char = word[i]
		n_char = word[i+1]
		word_prime = word[:i] + n_char + b_char + word[i+2:]
		if word_prime in words:
				arr.add(word_prime)

def no_typo(arr, word):
	if word in words:
		arr.add(word)

words = set()
typos = []

with open('words_alpha.txt', 'r') as f:
	for w in f.read().split('\n'):
		words.add(w)
with open('typos.json', 'r') as f:
	typos = f.read()[1:-1].replace("'", '').replace(' ', '').split(',')

corrections = dict()
for typo in typos:
	possibilities = set()
	missing_char(possibilities, typo)
	added_char(possibilities, typo)
	wrong_char(possibilities, typo)
	swapped_char(possibilities, typo)
	no_typo(possibilities, typo)

	possibilities = list(possibilities)
	if len(possibilities) == 1:
		possibilities = possibilities[0]
	corrections[typo] = possibilities

corr = str(corrections)
formated = corr.replace("'", '"')
print(formated)
