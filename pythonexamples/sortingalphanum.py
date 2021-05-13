s=input('Enter alphanumeric string:')
alphabets=[]
digits=[]
for ch in s:
	if ch.isalpha():
		alphabets.append(ch)
	else:
		digits.append(ch)
#print(alphabets) ['B','A','D']
#print(digits)    ['4','1','3']
output=''.join(sorted(alphabets)+sorted(digits))
print(output) 
