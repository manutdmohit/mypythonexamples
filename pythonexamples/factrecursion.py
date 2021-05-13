def fact(n):
	if n==0:
		result=1
	else:
		result=n*fact(n-1)
	return result
print('The Factorial of 3 is:',fact(3))
for i in range(11):
	print('The Factorial of {} is {}'.format(i,fact(i))) 