count=0
def fact(n):
	global count
	count=count+1
	print('Executing Factorial Function for n :',n) 
	if n==0:
		result=1
	else:
		result=n*fact(n-1)
	return result
print(fact(994))
print(count)
 