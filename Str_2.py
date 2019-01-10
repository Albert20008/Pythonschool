s = input('Введите что-нибудь: ')
i = 0
j = - 1
Palingrom = True
for g in range(-1, len(s), 2):
	while s[i] == ' ':
		i = i + 1
	while s[j] == ' ':
		j = j - 1
	if s[i] == s[j]:
		i = i + 1
		j = j - 1
	else:
		Palingrom = False
		break
if Palingrom:
	print('Это Палиндром')
else:
	print('Это не Палиндром')