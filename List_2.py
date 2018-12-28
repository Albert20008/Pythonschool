import random
a = []
n = int(input('Введите число: '))
for i in range(n):
	a.append(random.randint(0,100))
for i,elem in enumerate(a):
	print('{}. {}'.format(i + 1, elem))
n = int(input('Поиск: '))
start = False
for i,elem in enumerate(a):
	if elem == n:
		start = True
		print(i + 1)
if not start:
	print('Такого числа нет(')