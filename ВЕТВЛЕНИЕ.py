x = 1600
if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
    print ("год высокосный")
else:
    print ("год невысокосный")