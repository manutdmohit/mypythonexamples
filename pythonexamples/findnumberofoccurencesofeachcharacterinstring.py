s='ABBACBA'
l=[]
for ch in s:
	if ch not in l:
		l.append(ch)
print(l)
for ch in l:
	print('{} occurs {} times'.format(ch,s.count(ch)))
