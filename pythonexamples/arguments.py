def f1(x,*y):
	print(x)
	print(y)
	for y1 in y:
		print(y1)
f1(10,20,30,40)
f1(10)
f1()