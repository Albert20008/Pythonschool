num = int(input('Введите число: '))

int_f = num
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'fourfeen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
gesat = ['', '', 'twenty', 'thirty', 'fourty', 'fivty', 'sixty', 'seventy', 'eightty', 'ninety']
mnogo = ['hundned', 'theusand', 'million', 'billion']

end = []

if int_f > 9999999999:
	print('Многовато:)')
else:
	#billion
	if int_f // 1000000000 > 0:
		end.append(ones[int_f // 1000000000])
		end.append(mnogo[3])
	#hundned_million
	if int_f // 100000000 % 10 > 0:
		end.append(ones[int_f // 100000000 % 10])
		end.append(mnogo[0])
	#gesat or teens, ones
	if int_f // 10000000 % 10 == 1:
		end.append(teens[int_f // 1000000 % 10])
	else:
		end.append(gesat[int_f // 10000000 % 10])
		end.append(ones[int_f // 1000000 % 10])
	if int_f // 1000000 > 0:
		end.append(mnogo[2])
	#theusand
	if int_f // 100000 % 10 > 0:
		end.append(ones[int_f // 100000 % 10])
		end.append(mnogo[0])
	#gesat or teens, ones
	if int_f // 10000 % 10 == 1:
		end.append(teens[int_f // 1000 % 10])
	else:
		end.append(gesat[int_f // 10000 % 10])
		end.append(ones[int_f // 1000 % 10])
	if int_f // 1000 % 1000 > 0:
		end.append(mnogo[1])
	#ones
	if int_f // 100 % 10 > 0:
		end.append(ones[int_f // 100 % 10])
		end.append(mnogo[0])
	if int_f // 10 % 10 == 1:
		end.append(teens[int_f % 10])
	else:
		end.append(gesat[int_f // 10 % 10])
		end.append(ones[int_f % 10])
	end = " ".join(end)
	print(end)