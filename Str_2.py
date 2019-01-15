s = input('Введите что-нибудь: ')

i = 0
j = len(s) - 1

while i < j:

	while s[i] == ' ':
		i = i + 1

	while s[j] == ' ':
		j = j - 1

	if not s[i] == s[j]:
		break
	i = i + 1
	j = j - 1

if i >= j:
	print('Это Палиндром')
else:
	print('Это не Палиндром')