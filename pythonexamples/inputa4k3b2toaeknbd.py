s=input('Enter string with required assumptions:')
output=''
for ch in s:
	if ch.isalpha():
		output=output+ch
		x=ch
	else:
		d=int(ch)
		newc=chr(ord(x)+d)
		output=output+newc
print(output)


