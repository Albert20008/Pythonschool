s = input('Введите что-нибудь: ')
s_1 = input('Введите символ: ')
g = 0
for elem in s:
	if elem == s_1:
		g = g + 1
print(g)