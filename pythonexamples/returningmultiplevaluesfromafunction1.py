def calc(a,b):
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return sum,sub,mul,div
t=calc(20,10)
print(type(t))
print(t)
for x in t:
	print(x)