import requests, json

# actions: {
#                 getFlag: function(t) {
#                     var e = t.commit;
#                     o.get("/flag").then(function(t) {
#                         alert(t.data.FLAG),
#                         e("setState", t.data)
#                     }).catch(function(t) {
#                         alert("Cannot afford $2000 flag.")
#                     })
#                 },
#                 load: function(t) {
#                     var e = t.commit;
#                     t.state;
#                     o.get("/load").then(function(t) {
#                         e("setState", t.data)
#                     })
#                 },
#                 deal: function(t) {
#                     var e = t.commit
#                       , a = t.state;
#                     o.post("/deal", {
#                         bet: a.bet
#                     }).then(function(t) {
#                         e("setState", t.data)
#                     })
#                 },
#                 hit: function(t) {
#                     var e = t.commit;
#                     t.state;
#                     o.post("/hit").then(function(t) {
#                         e("setState", t.data)
#                     })
#                 },
#                 hold: function(t) {
#                     var e = t.commit;
#                     t.state;
#                     o.post("/hold").then(function(t) {
#                         e("setState", t.data)
#                     })
#                 }

def flag():
	resp = s.get(f'{url}flag')
	return resp.text

def load():
	resp = s.get(f'{url}load')
	return json.loads(resp.text)

def deal(bet):
	resp = s.post(f'{url}deal', data={'bet': bet})
	return json.loads(resp.text)

def hit():
	resp = s.post(f'{url}hit')
	return json.loads(resp.text)

def hold():
	resp = s.post(f'{url}hold')
	return json.loads(resp.text)

def get_value(hand):
	values = {'A': 11 if len(hand) == 2 else 1, '2': 2, '3': 3, '4': 4, '5': 5,
				'6': 6, '7': 7, '8': 8, '9': 9,
				'J': 10, 'Q': 10, 'K': 10, '10': 10}
	total = 0
	soft = False
	for c in hand:
		c = c['rank']
		if c == 11:
			soft = True
		total += values[c]
	return -total if soft else total

def play(p_hand, d_hand):
	p_value = get_value(p_hand)
	d_value = abs(get_value(d_hand))

	if p_value > 0:
		if p_value >= 18:
			return hold()
		elif p_value >= 17:
			if d_value >= 7:
				return hit()
			else:
				return hold()
		else:
			return hit()
	else:
		p_value = abs(p_value)
		if p_value >= 19:
			return hold()
		elif p_value == 18:
			if d_value >= 10:
				hit()
			else:
				hold()
		else:
			hit()


global s
url = 'https://blackjack-server.unitedctf.ca/'

while True:
	s = requests.Session()
	ctr = 0
	game = load()
	c = game['cash']
	m = 0
	while c > 50:
		ctr += 1
		c = game['cash']
		m = max(m, c)
		if c >= 2000:
			print(flag())
			break
		game = deal(50)
		while game['state'] == 'IN_GAME':
			game = play(game['playerHand'], game['dealerHand'])
	print(f"Lost after {ctr} games...\nMax was: {m}\n{'-'*50}")

print(f"Winning advantage: {game['cash'] - 1000} over {n} games.")
