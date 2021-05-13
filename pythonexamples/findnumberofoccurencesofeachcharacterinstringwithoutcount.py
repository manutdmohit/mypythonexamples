s=input('Enter some string:')
d={}
for ch in s:
	d[ch]=d.get(ch,0)+1
for k,v in d.items():
	print('{} occurs {} times'.format(k,v))