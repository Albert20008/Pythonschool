n = int(input("n = "))
for i in range(n,0,-1):
    for e in range(i):
        print('*',end = "")
    print ()
for j in range(1,n):
    for i in range(j+1):
        print('*',end = "")
    print ()
