vowels=['a','e','i','o','u']
word=input('Enter any string:')
result=[ch for ch in vowels if ch in word]
print(result)
print('The number of unique vowels:',len(result))
