def sym(n):
	if n < 10:
		return n
	else:
		return sym(n // 10) + n % 10
n = int(input("Введите число: "))
print(sym(n))