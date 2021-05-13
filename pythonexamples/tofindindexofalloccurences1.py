s='ABCABCABCA'
subs=input('Enter substring to search: ')
i=s.find(subs)
if i==-1:
	print('substring not found')
while i!=-1:
	print('{} present at index:{}'.format(subs,i))
	i=s.find(subs,i+len(subs),len(s))
	print('The number of occurences:',s.count(subs))

	
