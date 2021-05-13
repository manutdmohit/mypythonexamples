s=input('Enter some string:')
d={}
for ch in s:
	d[ch]=d.get(ch,0)+1
output=''
for k,v in d.items(): #for k,v in sorted(d.items()):
	output=output+str(v)+k
print(output)
	