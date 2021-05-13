d={100:'durga',200:'ravi',300:'shiva'}
key=int(input('Enter key to find value:'))
if key in d:
	print('The corresponding value:',d[key])
else:
	print('The specified key not available')