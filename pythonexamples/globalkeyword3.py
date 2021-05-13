a=777
def f1():
	global a
	print(a)
	a=999
	print(a)
f1()
