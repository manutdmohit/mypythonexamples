s=input('Enter any character: ')
if s.isalnum():
	print('It is alphanumeric character')
	if s.isalpha():
			print('It is alpha character')
			if s.islower():
					print('It is lowercase character')
			else:
					print('It is uppercase character')
	else:
		print('It is a digit')
elif s.isspace():
		print('It is space character')
else:
		print('It is non-space special character')

	







				


