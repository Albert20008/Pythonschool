f = int(input('Введите число: '))
my_list = []
for i in range(f - 2, -1, -1):
    my_list += [f - i]
for i in range(len(my_list)):
	for g in range(i + 1, len(my_list)):
		if my_list[g] == '':
			break
		elif my_list[g] % my_list[i] == 0:
			del my_list[g]
			my_list += ['']
for i in range(len(my_list)):
	if my_list[i] != '':
		print(my_list[i])