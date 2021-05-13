def fact(num):
	result=1
	while num>=1:
		result=result*num
		num=num-1
	return result
print('The factorial of 3 is',fact(3))
for i in range(1,6):
	print('The Factorial of', i,'is',fact(i))

