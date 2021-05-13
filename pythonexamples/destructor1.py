class Test:
	def __init__(self):
		print('Object Initialiaztion Activities')
	def __del__(self):
		print('Fulfilling last wish and Performing cleanup activities....')
t1=Test()
t2=Test()
t1=None
t2=None
print('End of application')



