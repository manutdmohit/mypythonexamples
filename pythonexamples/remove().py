l=[1,2,3,4,5,6]
print('Before removal:',l)
x=int(input('Enter element to remove:'))
if x in l:
	l.remove(x)
	print('After removal:',l)
else:
	print(x,'not present in the list')



