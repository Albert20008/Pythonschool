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
			if i == len(s) or j == - (len(s)):
				start = False
				print('Это Палиндром')
	else:
		print('Это не Палиндром')
		start = False