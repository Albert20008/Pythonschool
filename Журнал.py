import struct

def menu_print() -> int:

	print('''
1 Список участников
2 Добавить студента
3 Редактировать студента
4 Удалить студента
5 Список отличников
6 Список неуспевающих
7 Выход
''')

	return int(input('>>> '))

def journal_str_print(student: int):

	print('{}. {} {} {} ({})'. format(student + 1, journal[student]['Фамилия'], journal[student]['Имя'], journal[student]['Отчество'], journal[student]['Группа']))


def journal_print(student: int):

	print("=== {} ===".format(student + 1))

	print('Фамилия: {}'.format(journal[student]['Фамилия']))

	print('Имя: {}'.format(journal[student]['Имя']))

	print('Отчество: {}'.format(journal[student]['Отчество']))

	print('Группа: {}'.format(journal[student]['Группа']))

	print('Оценки:')

	if len(journal[student]['Оценки']) == 0:

		print('Нет оценок')

	else:

		for g, elem in journal[student]['Оценки'].items():

			print(' {}: {}'.format(g, elem))

def journal_student_edit(student: int):

	check = False

	while not check:

		journal_print(student)

		print('''
1 Изменить фамилию
2 Изменить имя
3 Изменить отчество
4 Изменить группу
5 Добавить оценку
6 Изменить оценку
7 Удалить оценку
8 Назад
''')

		modification = int(input('>>> '))

		if modification == 1:

			command = input('Введите новое: ')
			journal[student]['Фамилия'] = command

		elif modification == 2:

			command = input('Введите новое: ')
			journal[student]['Имя'] = command

		elif modification == 3:

			command = input('Введите новое: ')
			journal[student]['Отчество'] = command

		elif modification == 4:

			command = input('Введите новую: ')
			journal[student]['Группа'] = command

		elif modification == 5:

			cheak = False
			while not cheak:

				command = input('Введите название предмета: ')

				if command not in journal[student]['Оценки']:

					command_1 = int(input('Введите оценку: '))
					while command_1 <= 0:

						print('Ошибка\nВведите число, которое больше 0')
						command_1 = int(input('Введите оценку: '))

					journal[student]['Оценки'][command] = command_1

					cheak = True

				else:

					print('У этого предмета уже есть оценка\nВведите предмет без оценки')

		elif modification == 6:

			cheak = False
			while not cheak:

				command = input('Введите название предмета: ')
				if command in journal[student]['Оценки']:

					command_1 = int(input('Введите оценку: '))
					while command_1 <= 0:

						print('Ошибка\nВведите число, которое больше 0')
						command_1 = int(input('Введите оценку: '))

					journal[student]['Оценки'][command] = command_1

					cheak = True

				else:

					print('У этого предмета нет оценка\nВведите предмет с оценкой')

		elif modification == 7:

			cheak = False
			while not cheak:

				command = input('Введите название предмета: ')
				if command in journal[student]['Оценки']:

					rubbish = input('Вы уверены? (да/нет): ')

					if rubbish == 'Да' or rubbish == 'да' or rubbish == 'ДА':

						del journal[student]['Оценки'][command]
						cheak = not(cheak)

					elif rubbish == 'Нет' or rubbish == 'нет' or rubbish == 'НЕТ':

						cheak = not(cheak)

					else:

						print('Введите да или нет!')

				else:

					print('Этот предмет не ведётся у этого студента')

		elif modification == 8:

			check = True

		else:

			print('Команда неверна')

		end()

def add_student():

	journal.append({})

	command = input('Укажите фамилию: ')
	journal[-1]['Фамилия'] = command

	command = input('Укажите имя: ')
	journal[-1]['Имя'] = command

	command = input('Укажите отчество: ')
	journal[-1]['Отчество'] = command

	command = input('Укажите группу: ')
	journal[-1]['Группа'] = command

	journal[-1]['Оценки'] = {}

def journal_Excellent():

	for i in range(len(journal)):

		cheak = True

		for g in journal[i]['Оценки'].values():

			if g != 5:

				cheak = False
				break

		if cheak:

			journal_str_print(i)

def journal_Underperforming():

	for i in range(len(journal)):

		cheak = True

		for g in journal[i]['Оценки'].values():

			if g <= 2:

				cheak = False
				break

		if cheak == False:

			journal_str_print(i)

def end():

	file = open('Журнал', 'wb')

	file.write(struct.pack('h', len(journal)))

	for i in range(len(journal)):

		for j in journal[i]:

			if j == 'Оценки':

				file.write(struct.pack('h', len(journal[i]['Оценки'])))

				for g in journal[i][j]:

					schoolwork = g.encode("utf-8")

					file.write(struct.pack('h{}sh'. format(len(schoolwork)), len(schoolwork), schoolwork, journal[i][j][g]))

			else:

				schoolwork = journal[i][j].encode('utf-8')

				file.write(struct.pack('h{}s'. format(len(schoolwork)), len(schoolwork), schoolwork))

	file.close()


journal = []

try:

	file = open('Журнал', 'rb')

except FileNotFoundError as e:

	pass

else:

	data = struct.unpack('h', file.read(2))
 
	for i in range(data[0]):

		journal.append({})

		data = struct.unpack('h', file.read(2))
		journal[i]['Фамилия'] = struct.unpack('{}s'. format(data[0]), file.read(data[0]))[0].decode("utf-8")

		data = struct.unpack('h', file.read(2))
		journal[i]['Имя'] = struct.unpack('{}s'. format(data[0]), file.read(data[0]))[0].decode("utf-8")

		data = struct.unpack('h', file.read(2))
		journal[i]['Отчество'] = struct.unpack('{}s'. format(data[0]), file.read(data[0]))[0].decode("utf-8")

		data = struct.unpack('h', file.read(2))
		journal[i]['Группа'] = struct.unpack('{}s'. format(data[0]), file.read(data[0]))[0].decode("utf-8")

		data = struct.unpack('h', file.read(2))
		journal[i]['Оценки'] = {}
	 	
		for j in range(data[0]):

			data = struct.unpack('h', file.read(2))
			schoolwork = struct.unpack('{}s'. format(data[0]), file.read(data[0]))[0].decode("utf-8")
			journal[i]['Оценки'][schoolwork] = struct.unpack('h', file.read(2))[0]

	file.close()

command_menu = 0

while command_menu != 7:

	command_menu = menu_print() 

	if command_menu == 1:

		if len(journal) == 0:

			print('Студентов нет')

			continue

		for i in range(len(journal)):

			journal_print(i)

	elif command_menu == 2:

		add_student()
		end()

	elif command_menu == 3:

		if len(journal) == 0:

			print('Студентов нет')

			continue

		student_menu = int(input('Введите номер студента: ')) - 1
		if student_menu < len(journal) and student_menu >= 0:

			journal_student_edit(student_menu)

		else:

			print('Студента с таким номером нет!')


	elif command_menu == 4:

		if len(journal) == 0:

			print('Студентов нет')

			continue

		for i in range(len(journal)):

			journal_str_print(i)

		student_menu = int(input('Введите номер студента: '))

		cheak = False
		while not cheak:

			rubbish = input('Вы уверены? (да/нет): ')

			if rubbish == 'Да' or rubbish == 'да' or rubbish == 'ДА':

				del journal[student_menu - 1]

				cheak = True

			elif rubbish == 'Нет' or rubbish == 'нет' or rubbish == 'НЕТ':

				cheak = True

			else:

				print('Введите да или нет!')

		end()

	elif command_menu == 5:

		if len(journal) == 0:

			print('Студентов нет')

			continue

		journal_Excellent()

	elif command_menu == 6:

		if len(journal) == 0:

			print('Студентов нет')

			continue

		journal_Underperforming()

	elif command_menu == 7:

		end()

	else:

		print('Команда неверна')


# journal = [
# {'Фамилия': 'Пупкин',
# 'Имя': 'Вася',
# 'Отчество': 'Фёдорович',
# 'Группа': 'АР-124',
# 'Оценки': {
# 'Математика': 4,
# 'Русский язык': 5}
# }]