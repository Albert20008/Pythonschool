list_player = {}

i = input('Введите имя игрока: ')

while i != 'exit':

	points = int(input('Введите его очки: '))

	list_player[i] = points

	i = input('Введите имя игрока: ')

for i, elem in list_player.items():

	print('{}: {}'.format(i, elem))
