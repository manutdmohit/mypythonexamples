a=888
def f1():
	a=100
	print(a)
print(globals())
print(globals().get('a'))
print(globals()['a'])

f1()