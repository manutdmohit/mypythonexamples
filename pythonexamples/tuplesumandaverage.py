t=eval(input('Enter Tuple of numbers:'))
sum=0
for x in t:
	sum=sum+x
print('sum=',sum)
print('Average=',sum/len(t))