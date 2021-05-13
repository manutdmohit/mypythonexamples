mail=input('Enter your mail id:')
try:
	i=mail.index('@')
	print('mail id contains @ symbol, which is mandatory')
except ValueError:
	print('mail id does not contain @ symbol')