def decor1(func):
	def inner1():
		print('decorator1 execution')
		func()
	return inner1
def decor2(func):
	def inner2():
		print('decorator 2 execution')
		func()
	return inner2

@decor2
@decor1
def f():
	print('Original Function')
f()
