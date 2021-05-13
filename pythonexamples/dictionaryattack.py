from random import *
digits='0123456789'
def get_fake_mno():
	mno='9841'
	for i in range(6):
		mno=mno+choice(digits)
	return mno
for i in range(100):
	print(get_fake_mno())