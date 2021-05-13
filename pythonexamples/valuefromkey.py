d={100:'A',200:'B',300:'C',400:'D'}
key=int(input('Enter key to find value:'))
if key in d:
	print('The corresponding value:',d.get(key))#d[key]
else:
	print('The key is not present')

