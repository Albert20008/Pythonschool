s = input('Введите что-нибудь: ')

i = 0
j = - 1
l = len(s) - 1

while i <= l // 2:

	while s[i] == ' ':
		i = i + 1

	while s[j] == ' ':
		j = j - 1

	if s[i] == s[j]:
		i = i + 1
		j = j - 1
	else:
		#Palingrom = False
		break

if i > l // 2:
	print('Это Палиндром')
else:
	print('Это не Палиндром')