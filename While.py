num = int(input("Введите любое число,кроме нуля: "))
end_num = num
while num != 0:
 	num = int(input("Введите любое число,кроме нуля: "))
 	end_num = end_num + num
print('Ты всё сломал!!!')
print(end_num)