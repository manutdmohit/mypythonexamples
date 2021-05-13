s=input('Enter any string:')
l=[]
for ch in s:
	if ch not in l:
		l.append(ch)
output=''.join(l)
print(output)