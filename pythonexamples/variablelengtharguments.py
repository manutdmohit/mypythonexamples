def f1(*n):
	print('variable length argument function')
	print(type(n))
	print(n)
f1()
f1(10)
f1(10,20,30,40)