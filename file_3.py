fail = open('файл №2', 'w')

n = input('Введите число: ')

while n != 'F':

	fail.write(n + ' ')

	n = input('Введите число: ')

fail.close()
