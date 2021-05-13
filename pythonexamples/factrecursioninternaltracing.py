def fact(n):
	print('Executing Factorial Function with n value:',n) 
	if n==0:
		result=1
	else:
		result=n*fact(n-1)
	print('Returning Result of fact({}) is {}'.format(n,result))
	return result
print(fact(3))
 