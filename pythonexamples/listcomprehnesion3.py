s='the quick brown fox jumps over the lazy dog'
words=s.split()
print(words)
l=[[word.upper(),len(word)] for word in words] 
print(l)