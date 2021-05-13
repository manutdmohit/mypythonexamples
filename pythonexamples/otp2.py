from random import *
otp=''
for i in range(6):
	otp=otp+str(randint(0,9))
print(otp)