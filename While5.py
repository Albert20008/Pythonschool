n = int(input('n = '))
m = int(input('m = '))
s = 1
def fact(s,e):
	i = 0
	for i in range(1 , e + 1):
		s = s * i
	return(s)
end = fact(s,n) / (fact(s,m) * fact(s,m - n))
print(end)