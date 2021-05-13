l=[10,20,0,5,0,30]
for x in l:
	if x==0:
		print('Hello Stupid, zero division error will occur')
		continue
	print('100/{}={}'.format(x,100//x))