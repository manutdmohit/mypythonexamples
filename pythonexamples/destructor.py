import time
class Test:
	def __init__(self):
		print('Object Initialiaztion Activities')
	def __del__(self):
		print('Fulfilling last wish and Performing cleanup activities....')
t=Test()
t=None
time.sleep(10)
print('End of application')



