from functools import reduce

# for i in range(f - 2, -1, -1):
# 	my_list += [f - i]

# for i in range(len(my_list)):

#  	for g in range(i + 1, len(my_list)):

#  		if my_list[g] == '':
#  			break

#  		elif my_list[g] % my_list[i] == 0:
#  			del my_list[g]
#  			my_list += ['']

def func(_list: list) -> bool:
	for i in range(len(my_list)):

		if my_list[i] == _list:
			continue

		a = _list % my_list[i] != 0

		if not a:
			break

	return a

f = int(input('Введите число: '))

my_list = range(2, f + 1)

my_list = list(filter(lambda x: reduce(lambda y, z: y and (x % z != 0 if x != z else True), my_list, True), my_list))

for i in range(len(my_list)):
  	print(my_list[i])
