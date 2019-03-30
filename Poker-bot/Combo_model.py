def combo(carts:list, carts_1:list) -> list:

	other = []

	other.extend(carts_1)

	other.extend(carts)

	check = False

	while not check:
	
		check = True
	
		for j in range(1, len(other)):
	
			if other[j - 1] < other[j]:
	
				d = other[j]
				other[j] = other[j - 1]
				other[j - 1] = d
	
				check = False

	major_cart = other[0]



	for j in range(len(other)):

		successively = [other[j]]

		for i in range(len(other)):

			if other[j][0] == other[i][0] + 1:

				j = i
				successively.append(other[i])

		if len(successively) >= 5:

			successively.append(True)
			break



	for i in range(len(other)):

		five_suit = []

		for j in range(len(other)):

			if other[i][2] == other[j][2]:

				five_suit.append(other[j])

		if len(five_suit) >= 5:

			five_suit.append(True)

			break 


	check = False
	if five_suit[-1] == True and successively[-1] == True:

		check = True

		for i in range(len(five_suit)):

			if five_suit[i] in successively:

				for g in range(len(successively)):
					
					if five_suit[i] == successively[g]:

						break

				start = [i, g]

				for g in range(g + 1, g + 6):

					i += 1

					if five_suit[i] != successively[g]:

						check = False
						break

				break

	if check:

		Roal = True

		for j in range(len(five_suit[start[0]:i])):

			if five_suit[j][0] < 10:

				Roal = False

		if Roal:

			return ['Роял-Флэш', five_suit[start[0]:i], major_cart, 10]

		else:

			return['Стрит-Флэш', five_suit[start[0]:i], major_cart, 9]

	elif five_suit[-1] == True:

		del five_suit[-1]

		return ['Флэш', five_suit, major_cart, 6]

	elif successively[-1] == True:

		del successively[-1]
		return ['Стрит', successively, major_cart, 5]




	for i in range(len(other)):

		four = []

		for j in range(len(other)):

			if other[i][0] == other[j][0]:

				four.append(other[j])

		if len(four) == 4:

			return ['Каре', four, major_cart, 8]




	check = False

	for i in range(len(other)):

		for j in range(len(other)):

			if i == j:
				continue

			if other[i][0] == other[j][0]:

				for g in range(len(other)):

					if g == i or g == j:
						continue

					if other[i][0] == other[g][0]:

						three = [i, j, g]
						check = True
						break

				if check:
					break

		if check:
			break




	if check:

		for i in range(len(other)):

			if i in three:
				continue

			for j in range(len(other)):

				if j in three or j == i:
					continue

				if other[i][0] == other[j][0]:

					three = [other[three[0]], other[three[1]], other[three[2]], other[i], other[j]]
					return ['Фулл-хаус', three, major_cart, 7]

		three = [other[three[0]], other[three[1]], other[three[2]]]
		return ['Тройка', three, major_cart, 4]




	check = False

	for i in range(len(other)):

		for j in range(len(other)):

			if i == j:
				continue

			if other[i][0] == other[j][0]:

				two_twain = [i, j]
				check = True
				break

		if check:

			for i in range(len(other)):
			
				if i in two_twain:
					continue

				for j in range(len(other)):
					
					if j in two_twain or j == i:
						continue

					if other[i][0] == other[j][0]:

						two_twain = [other[two_twain[0]], other[two_twain[1]], other[i], other[j]]
						return ['Две пары', two_twain, major_cart, 3]

			two_twain = [other[two_twain[0]], other[two_twain[1]]]
			return ['Пара', two_twain, major_cart, 2]

	return ['Старшая карта', [major_cart], major_cart, 1]
