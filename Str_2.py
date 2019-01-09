s = input('Введите что-нибудь: ')
i = 0
j = - 1
while i < len(s) // 2:
	while s[i] == ' ':
		i = i + 1
	while s[j] == ' ':
		j = j - 1
	if s[i] == s[j]:
		i = i + 1
		j = j - 1
	else:
		break
if i >= len(s) // 2:
	print('Это Палиндром')
else:
	print('Это не Палиндром')