d={100:'A',200:'B ',300:'C',400:'D'}
value=input('Enter value to find key:')
available=False
for k,v in d.items():
	if v==value:
		print('The corresponding key',k)
		available=True
if available==False:
	print('The specified value not found in dict')
