l=[0,1,2,3,4,5,6,7,8,9,10]
def isEven(n):
	if n%2==0:
		return True
	else:
		return False
l1=[]
for n in l:
	if isEven(n)==True:
		l1.append(n)
print(l1)