def sym_num(e):
	if e < 10:
		print(e)
	else:
		s = e % 10
		print(s, end = '')
		sym_num(e // 10)
n = int(input('Введите число: '))
sym_num(n)