Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='ram'
>>> r=reversed(s)
>>> for ch in r:
	print(ch):
		
SyntaxError: invalid syntax
>>> for ch in r:
	print(ch);

	
m
a
r
>>> s='Learning Python Is Very Easy'
>>> l=s.split()
>>> print(l)
['Learning', 'Python', 'Is', 'Very', 'Easy']
>>> l=s.split('.')
>>> print(l)
['Learning Python Is Very Easy']
>>> l=s.split()
>>> print(l)
['Learning', 'Python', 'Is', 'Very', 'Easy']
>>> s='Learning Python Is Very Easy'
>>> s.append('rahul')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.append('rahul')
AttributeError: 'str' object has no attribute 'append'
>>> s.append(rahul)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.append(rahul)
AttributeError: 'str' object has no attribute 'append'
>>> s=['Learning','Python', 'is','Easy')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> s=['Learning','Python', 'is','Easy']
>>> s.append('rahul')
>>> print(s)
['Learning', 'Python', 'is', 'Easy', 'rahul']
>>> s
['Learning', 'Python', 'is', 'Easy', 'rahul']
>>> ' '.join(s)
'Learning Python is Easy rahul'
>>> s=['Learning','Python', 'is','Easy']
>>> s[0]
'Learning'
>>> a=s[1]
>>> a[::-1]
'nohtyP'
>>> s[0]+a+s[2:]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s[0]+a+s[2:]
TypeError: can only concatenate str (not "list") to str
>>> s[0]+s[1]+s[2:]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[0]+s[1]+s[2:]
TypeError: can only concatenate str (not "list") to str
>>> ' '.join(s[0],a,s[2])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ' '.join(s[0],a,s[2])
TypeError: join() takes exactly one argument (3 given)
>>> ' '.join(s)
'Learning Python is Easy'
>>> s=['Learning','Python', 'is','Easy']
>>> s1=[]
>>> for word in l
SyntaxError: invalid syntax
>>> for word in l:
	s1.append(word[2][::-1])

	
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    s1.append(word[2][::-1])
IndexError: string index out of range
>>> for word[2] in l:
	s1.append(word[2][::-1])

	
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    for word[2] in l:
TypeError: 'str' object does not support item assignment
>>> s='ram is a good boy'
>>> s[0]
'r'
>>> 