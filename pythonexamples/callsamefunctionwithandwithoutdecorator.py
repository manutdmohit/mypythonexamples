def decor(func):
	def inner(name):
		if name=='Sunny':
			print('Hi')
		else:
			func(name)
	return inner
	
def wish(name):
	print('Good Morning:',name)
decorated_wish=decor(wish)
wish('Durga')
wish('Sunny')
decorated_wish('Durga')
decorated_wish('Sunny')
