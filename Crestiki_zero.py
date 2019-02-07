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

		print('Игрок "{}" победил!!!'. format(player))

		break

if cheak == False:

	print('Ничья')
