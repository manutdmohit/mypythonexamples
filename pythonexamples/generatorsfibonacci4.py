def fibonacci_sequence_generator():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
g=fibonacci_sequence_generator()
'''for x in g:
	if x<=10:
		print(x)
	else:
		break'''
count=1
while count<=10:
	print(next(g))
	count=count+1