import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a == 0:
    if b == 0:
        if c == 0:
            print ("корень равен любому числу")
        else: 
            print ("корней нет")
    else:
        x = (-c) / b
        print ('x = {}'.format (x))
else:
    D = (b*b) - (4*a*c)
    if D > 0:
        x_1 = ((-b) + (math.sqrt(D))) / (2 * a)
        print ('x_1 = {}'.format (x_1))
        x_2 = ((-b) - (math.sqrt(D))) / (2 * a)
        print ('x_2 = {}'.format (x_2))
    elif D == 0:
        x = (-b) / (2 * a)
        print ('x = {}'.format (x))
    else:
        print ("Дискриминант меньше нуля,корней нет")
