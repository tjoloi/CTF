total = 0

with open('dataset.csv', 'r') as file:
	lines = file.readlines()[1:]

	for line in lines:
		line = line.replace('\n', '')
		items = line.split(',')
		jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
		if items[1]=='73' and items[2]=='Ligne orange' and items[-3] in jours:
			print(float(items[-1]))
			total += float(items[-1])
print(total)