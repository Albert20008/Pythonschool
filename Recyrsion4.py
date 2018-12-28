def sym_num(e):
	s = (e % 10 + 1) % 10
	if e >= 10:
		sym_num(e // 10)
	print(s, end = '')
n = int(input('Введите число: '))
sym_num(n)
print()





# def sym_num(e):
# 	if e < 10:
# 		print((e+1)%10, end="")
# 	else:
# 		sym_num(e // 10)
# 		print((s % 10 + 1) % 10, end='')

# def sym_num(e, y):
# 	# тут отбор числа
# 	if e % 10 == 9:
# 		s = 0
# 	else:
# 		s = e % 10 + 1		
# 	if e < y:
# 		print(s, end = '')
# 		#Конец функции
# 		if y * 10 > n:
# 			if n < 10:
# 				print()
# 			elif n % 10 == 9:
# 				e = 0
# 				print(e)
# 			else:
# 				print(n % 10 + 1)
# 		#повтор функции
# 		else:
# 			y = y * 10
# 			sym_num(n, y)
# 	else:		
# 		sym_num(e // 10, y)
# n = int(input('Введите число: '))
# a = 10
# sym_num(n, a)
