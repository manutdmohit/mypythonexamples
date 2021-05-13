def countdown_generator(num):
	while num>=1:
		yield 
		num=num-1
g=countdown_generator(10)
import time
for x in g:
	print(x)
	time.sleep(1)