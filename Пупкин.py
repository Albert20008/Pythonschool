def pup(n):
	if n == 1:
		return 5
	elif n == 2:
		return 7
	else:
		return pup(n - 1) * pup(n - 2) 
a = int(input('Введите число: '))
print(pup(a))