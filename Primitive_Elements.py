k = int(input("Enter a prime number"))
for j in range(2,k):
	a = {}
	l = 0
	for i in range(1,k):
		a[j**i%k] = 1
	for i in range(1,k):
		if( a.get(i ,0) != 0 ):
			l+=1
	if( l == k-1):
		print(j)