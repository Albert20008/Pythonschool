import random
print('Здравствуйте, мистер Свалов\nВы просили сделать программу для упорядочевания данных в массиве\nВсё уже сделано)\nДля удобства мы решили внести в массив случайный набор чисел\nОсталось только ввести количество этих чисел\nИ это мы решили предоставить вам')
a = []
n = int(input('Введите количество случайных чисел мистер Свалов: '))
for i in range(n):
	a.append(random.randint(0,100))
for i,elem in enumerate(a):
	print('{}. {}'.format(i + 1, elem))
right = False
while not right:
	right = True
	for j in range(1, len(a)):
		if a[j - 1] > a[j]:
			d = a[j]
			a[j] = a[j - 1]
			a[j - 1] = d
			right = False
print(a)
# import random
# a = []
# n = int(input('Введите число: '))
# for i in range(n):
# 	a.append(random.randint(0,100))
# for i,elem in enumerate(a):
# 	print('{}. {}'.format(i + 1, elem))
# f = True
# while f != False:
# 	f = n
# 	for j in range(1, len(a)):
# 		if a[j - 1] > a[j]:
# 			d = a[j]
# 			a[j] = a[j - 1]
# 			a[j - 1] = d
# 		else:
# 			f = f - 1
# 	if f == 1:
# 		f = False
# print(a)