class Test:
	def __init__(self):
		print('The address of object pointed by self:',id(self))
t=Test()
print('The address of object pointed by test:',id(t))