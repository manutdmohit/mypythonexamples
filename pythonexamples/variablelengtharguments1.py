def sum(*n):
	total=0
	for x in n:
		total=total+x
	print('The sum:',total)
sum()
sum(10)
sum(10,20)
sum(10,20,30,40,50,60)