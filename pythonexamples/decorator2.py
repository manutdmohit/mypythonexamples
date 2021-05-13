def decor(func):
	def inner(name):
		names=['CM','PM','Minister']
		if name in names:
			print('#'*50)
			print('Hello {}, you are very important for us'.format(name))
			print('Very Very Good Morning')
			print('#'*50)
		else:
			func(name)
	return inner

@decor
def wish(name):
	print('Good Morning:',name)
wish('CM')
wish('Sunny')