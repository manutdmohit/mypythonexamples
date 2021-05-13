vowels=['a','e','i','o','u']
word=input('Enter any string:')
result=[]
for ch in word:
	if ch in vowels:
		if ch not in result:
			result.append(ch)
print(result)
print('The number of unique vowels:',len(result))