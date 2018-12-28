s = input('Введите что-нибудь: ')
i = 0
j = - 1
start = True
while start:
	while s[i] == ' ':
		i = i + 1
	while s[j] == ' ':
		j = j - 1
	if s[i] == s[j]:
		i = i + 1
		j = j - 1
		start = i < len(s)
	else:
		start = False
		print('Это не Палиндром')
if i == len(s):
	print('Это Палиндром')