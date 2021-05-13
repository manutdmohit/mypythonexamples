l=[1,2,2,2,3,3]
x=int(input('Enter element to find :'))
if x in l:
	print('{} present at index:{}'.format(x,l.index(x)))
else:
	print(x,'not available in list')