n=int(input('Enter n value:'))
count=0
n1=2
while True:
	#This code is responsible to check whether n1 is prime or not
	is_prime=True
	for i in range(2,n1//2+1):
		if(n1%i==0):
			is_prime=False
			break
	if is_prime==True:
		print(n1)
		count=count+1
	if count==n:
		break
	n1=n1+1













