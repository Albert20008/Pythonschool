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

#ЭТО ОДИН КОД!!!!

# while not check:

#  	check = True

#  	for i in range(len(chart) - 1, -1, -1):

#  		final_1 = 0

#  		for g in range(len(chart[i])):

#  			final += chart[i][g]

#  		for g in range(i - 1, -1, -1):

#  			for j in range(len(chart[g])):

#  				final_1 += chart[g][j]

#  			if final > final_1:

#  				d = chart[g]
#  				chart[g] = chart[i]
#  				chart[i] = d
#  				check = False

#А ВОТ ЭТО ДРУГОЙ КОД!!!!

# for i in range(len(chart)):

# 	final = 0
# 	final_command = -1

# 	for g in range(len(chart[i])):

# 		final += chart[i][g]

# 	for g in range(i + 1, len(chart)):

# 		final_1 = 0

# 		for j in range(len(chart[g])):

# 			final_1 += chart[g][j]

# 		if final_1 > final:

# 			final = final_1
# 			final_command = command_list[g]

# 	if final_command != -1:

# 		d = chart[i]
# 		b = command_list[i]

# 		chart[i] = chart[final_command]
# 		command_list[i] = final_command

# 		chart[final_command] = d
# 		command_list[final_command] = b

# 	print('{} место занимает команда {}'. format(i + 1, command_list[i] + 1))

#А ВОТ ЭТО ДВА КОДА ВМЕСТЕ!!!)
check = False

while not check:

	check = True

	for i in range(len(chart) - 1):

		final_1 = 0
		final = 0

		for g in range(len(chart[i])):

			final += chart[i][g]

		for g in range(len(chart[i + 1])):

			final_1 += chart[i + 1][g]

		if final_1 > final:

			b = command_list[i] 
			d = chart[i]
			command_list[i] = command_list[i + 1]
			command_list[i + 1] = b
			chart[i] = chart[i + 1]
			chart[i + 1] = d
			check = False

for i in range(len(command_list)):

	print('{} место занимает команда {}'. format(i + 1, command_list[i] + 1))