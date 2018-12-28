import random
a = []
n = int(input('Введите число: '))
for i in range(n):
	a.append(random.randint(0,100))
for i,elem in enumerate(a):
	print('{}. {}'.format(i + 1, elem))
n = 0
for i in range(1, len(a)):
	if a[n] < a[i]:
		n = i
print('{}. {}'. format(n + 1, a[n]))