def clock(n,h):
    i = 0
    j = 0
    for i in range(n, 0, -2):
        for j in range(h):
            print(' ',end = "")
        for j in range(i):
            print('*',end = "")
        h = h + 1
        print ()
    h = h - 2
    for i in range(3, n+1, 2):
        for j in range(h):
            print(' ',end = "")
        for j in range(i):
            print('*',end = "")
        h = h - 1
        print ()

n = int(input("Введите нечётное число: "))
while n % 2 == 0:
    print('Ошибка, число должно быть нечётным!!!')
    n = int(input("Введите нечётное число: "))
h = 0
for i in range(0, n, 2):
    clock(n - i, h + i // 2)
for j in range(i - 2, - 1, - 2):
    clock(n - j , h + j // 2)