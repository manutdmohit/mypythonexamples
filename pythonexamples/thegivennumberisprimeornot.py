n=int(input('Enter any number: '))
if n<=1:
	print('It is not prime number')
else:
	is_prime=True
	for i in range(2,n//2+1): #from 2 to n-1     from 2 to n//2
		if n%i==0:
			is_prime=False
			break
	if is_prime==True:
		print('It is prime number:')
	else:
		print('It is not prime number:')

				