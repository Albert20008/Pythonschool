with open('файл №1', 'r') as fail:

	a = fail.read()
	a = a.split('\n')


fail = open('файл №1', 'w')

for i in range(len(a) - 1):

	a[i] = str(int(a[i]) * 2)

	fail.write(a[i] + '\n')

fail.close()
