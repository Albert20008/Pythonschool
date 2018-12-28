#n = int(input("Введите число: "))
#for i in range(n):
#	for j in range(n):
#		if j + i <= n - 1:
#			print('*',end = '')
#		else:
#	print()
n = int(input("Введите число: "))
for i in range(n):
	for j in range(n):
		if (j + i == n - 1 or j == i) or (j == 0 or j == n - 1) :
			print('*', end = '')
		else:
			print(',', end = '')
	print()
#(j == i and i < n // 2) or (j + i == n - 1 and i >= n // 2)
#j>= i
#(j + i <= n - 1 and j >= i) or (j + i <= n - 1 and j >= i) or j == i