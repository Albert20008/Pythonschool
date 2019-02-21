def pole_func():

	print('+-+-+-+')
	for i in range(3):

		for g in range(len(cells[i])):

			print('|', end = '')
			print(cells[i][g], end = '')

		print('|')
		print('+-+-+-+')
		


def cheak_pole(player: str) -> bool:

	for i in range(3):

		if cells[i][0] == player and cells[i][1] == player and cells[i][2] == player:

			return 1

		if cells[0][i] == player and cells[1][i] == player and cells[2][i] == player:

			return 1

	if cells[0][0] == player and cells[1][1] == player and cells[2][2] == player:
 
		return 1

	if cells[0][2] == player and cells[1][1] == player and cells[2][0] == player:

		return 1

	return 0

player_x = input('Игрок(x), ведите ваше имя: ')

player_o = input('Игрок(o), ведите ваше имя: ')

fieid_width = 3

cells = []

for i in range(fieid_width):

	cells.append([])
	for g in range(fieid_width):

		cells[i].append(' ')

pole_func()

cheak = False
for i in range(fieid_width * fieid_width):

	if i % 2 == 0:

		player = 'X'

	else:

		player = 'O'

	print('Ход игрока({})'. format(player))

	x = int(input('Х: '))
	y = int(input('Y: '))

	cheak_1 = False
	while cheak_1 == False:

		if x > fieid_width or y > fieid_width:

			print('Клетка несуществует')

			x = int(input('Х: '))
			y = int(input('Y: '))

		elif cells[y - 1][x - 1] != ' ':

			print('Клетки занята')

			x = int(input('Х: '))
			y = int(input('Y: '))

		else:

			cheak_1 = True

	cells[y - 1][x - 1] = player
	pole_func()

	cheak = cheak_pole(player)
	if cheak == True:

		if player == 'X':

			print('Игрок "{}" победил!!!'. format(player_x))
			player = player_x

		elif player == 'O':

			print('Игрок "{}" победил!!!'. format(player_o))
			player = player_o

		break

if cheak == False:

	print('Ничья')

print()

#Таблица игроков
players = {}

try:

	file = open('Таблица игроков.txt', 'r')

except FileNotFoundError as e:

	file = open('Таблица игроков.txt', 'w')

	file.close()

else:

	players_file = file.read()

	file.close()

	players_file = players_file.split('\n')

	for i in range(len(players_file) - 1):

		g = players_file[i].split(' ')

		players[g[0]] = g[1]
#Тут словарь собрался

players.setdefault(player, 0)

players[player] = int(players[player]) + 1

with open('Таблица игроков.txt', 'w') as file:

	for i in players:

		file.write('{} {}\n'. format(i, players[i]))

for i in players:

	print('{} {}'. format(i, players[i]))
