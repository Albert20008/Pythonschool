fail = open('файл №2', 'r')

Pre_content = fail.read()
Pre_content = Pre_content.split()

fail.close()

fail = open('файл №2', 'w')

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
gesat = ['', '', 'twenty', 'thirty', 'fourty', 'fivty', 'sixty', 'seventy', 'eightty', 'ninety']
mnogo = ['hundred', 'thousand', 'million', 'billion']

for i in range(len(Pre_content)):

	end = []

	num = int(Pre_content[i])

	if num == 0:

		fail.write('zero')

	else:

		if num < 0:
			num = -num

		#billion
		if num // 1000000000 > 0:
			end.append(ones[num // 1000000000])
			end.append(mnogo[3])
		#hundned_million
		if num // 100000000 % 10 > 0:
			end.append(ones[num // 100000000 % 10])
			end.append(mnogo[0])
		#gesat or teens, ones
		if num // 10000000 % 10 == 1:
			end.append(teens[num // 1000000 % 10])
		else:
			end.append(gesat[num // 10000000 % 10])
			end.append(ones[num // 1000000 % 10])
		#million_mnogo
		if num // 1000000 > 0:
			end.append(mnogo[2])
		#theusand
		if num // 100000 % 10 > 0:
			end.append(ones[num // 100000 % 10])
			end.append(mnogo[0])
		#gesat or teens, ones
		if num // 10000 % 10 == 1:
			end.append(teens[num // 1000 % 10])
		else:
			end.append(gesat[num // 10000 % 10])
			end.append(ones[num // 1000 % 10])
		#theusand_mnogo
		if num // 1000 % 1000 > 0:
			end.append(mnogo[1])
		#ones
		if num // 100 % 10 > 0:
			end.append(ones[num // 100 % 10])
			end.append(mnogo[0])
		if num // 10 % 10 == 1:
			end.append(teens[num % 10])
		else:
			end.append(gesat[num // 10 % 10])
			end.append(ones[num % 10])
		#конец
		if num < 0:

			fail.write('minus ')

		for g in range(len(end) - 1):

			if end[g] != '':

				fail.write(end[g] + ' ')

		fail.write(end[len(end) - 1])

	if i != len(Pre_content) - 1:

		fail.write(', ')

fail.close()
