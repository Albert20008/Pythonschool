a = []
n = int(input("Введите число: "))
while n != 0:
	a.append(n)
	n = int(input("Введите число: "))
for i,elem in enumerate(a):
	print('{}. {}'.format(i + 1, elem))
n = 0
for elem in a:
	n = n + elem
n = n / len(a)
print(n)