s=input('Enter some string in which alphabet symbol should be followed by digits:')
target=''
for ch in s:
	if ch.isalpha():
		x=ch
	else:
		d=int(ch)
		target=target+x*d 
output=''.join(sorted(target))
print(output)