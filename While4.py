#n = int(input('Введите число: '))
#i = 2
#n_1 = 1
#n_2 = 1
#while i != n:
#	if i != n:
#		i = i + 1
#		n_3 = n_1 + n_2
#	if i != n:
#		i = i + 1
#		n_1 = n_2 + n_3
#	if i != n:
#		i = i + 1
#		n_2 = n_3 + n_1
#if n_1 > n_3 and n_1 > n_2:
#	print(n_1)
#elif n_2 > n_1 and n_2 > n_3:
#	print(n_2)
#elif n_3 > n_2 and n_3 > n_1:
#	print(n_3)
n = int(input('Введите число: '))
def fib(a):
	i = 2
	n_1 = 1
	n_2 = 1
	while i < a:
		i = i + 2
		n_1 = n_1 + n_2
		n_2 = n_2 + n_1
	if n % 2 != 0:
		return(n_1)
	else:
		return(n_2)
n = fib(n)
print(n)