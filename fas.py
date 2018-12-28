import random
num = random.randint(1,100)
s = 0
start = False
while not start:
	num_u = int(input('Введите число: '))
	if num_u == num:
		print('Вы угадали')
		s = str(s + 1)
		print('У вас '+ s +' попыток')
		start = True
	elif num_u > num:
		print('Ваше число больше загаданого.')
		s = s + 1
	else:
		print('Ваше число меньше загаданого.')
		s = s + 1