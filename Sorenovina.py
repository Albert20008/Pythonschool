from random import randint

n = int(input('Введите кол-во команд: '))
sor = int(input('Введите кол-во этапов: '))

chart = []
final = 0

for i in range(n):

	chart.append([])

	for g in range(sor):

		chart[i].append(randint(1, 10))

#Это для заголовков
print()
print('№ команды:   Баллы:')
#Это для заголовков

for i in range(len(chart)):

	print('Команда "{}":'. format(i + 1), end = ' ')

	for g in range(len(chart[i])):

		print(chart[i][g], end = ' ')

	print()

final_command = -1
final = 0

for i in range(len(chart)):

	final_1 = 0

	for g in range(len(chart[i])):

		final_1 += chart[i][g]

	if final_1 > final:

		final_command = i
		final = final_1

print('Победитель команда {}'. format(final_command + 1))

final_list = []

for i in range(len(chart)):

	final = 0

	final_list.append([])

	for g in range(len(chart[i])):

		final += chart[i][g]

	final_list[i].append(str(i + 1))
	final_list[i].append(final)

check = False

while not check:

	check = True

	for i in range(len(final_list) - 1):

		if final_list[i][1] < final_list[i + 1][1]:

			b = final_list[i + 1]
			final_list[i + 1] = final_list[i]
			final_list[i] = b
			check = False

for i in range(len(final_list)):

	print('{} место занимает команда {}'. format(i + 1, final_list[i][0]))