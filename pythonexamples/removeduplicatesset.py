s={10,20,30,10,11,30}
s1=set()
for x in s:
	if x not in s1:
		s1.add(x)
print(s1)
