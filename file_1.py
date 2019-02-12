fail = open('файл №1', 'w')

n = input('Введите число: ')

while n != 'F':

	fail.write(n + '\n')

	n = input('Введите число: ')

fail.close()
