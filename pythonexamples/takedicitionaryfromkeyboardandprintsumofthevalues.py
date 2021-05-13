d=eval(input('Enter Dictionary:'))
sum=0
for item in d.items():
	sum=sum+item[1]
print('The sum of values:',sum)