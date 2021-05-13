word=input('Enter any string:')
d={}
for ch in word:
	d[ch]=d.get(ch,0)+1
print(d)
