Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='Ram is a "very very" good Boy'
>>> print(s)
Ram is a "very very" good Boy
>>> s='''Ram "is" a 'very very' good boy'''
>>> print(s)
Ram "is" a 'very very' good boy
>>> #triple quotes
>>> # to define multiple string literals
>>> to use 'and " as normal characters in our string
SyntaxError: invalid syntax
>>> #to use 'and " as normal characters in our string
>>> #doc string
>>> #Index#
>>> #access characters
>>> s='durga'
>>> print(s[0])
d
>>> print(s[100])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(s[100])
IndexError: string index out of range
>>> print(s[0])
d
>>> print(s[-1])
a
>>> #positive and negative support#
>>> #positive from left to right 0 to and negative from right to left -1 to
>>> print(s[-5]0
      
SyntaxError: invalid syntax
>>> print(s[-5])
d
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> #slice operator
>>> #getting part of slice
>>> s='abcdefghijklmnopqrstuvwxyz'
>>> # s[begin : end]
>>> # retunes sub string(slice) from begin index to end -1 index
>>> # returns sub string(slice) from begin index to end -1 index#
>>>  s[3:9]
 
SyntaxError: unexpected indent
>>> s[3:9]
'defghi'
>>> prin(s[3:9])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    prin(s[3:9])
NameError: name 'prin' is not defined
>>> print(s[3:9])
defghi
>>> s[ :9]
'abcdefghi'
>>> s[ 3:]
'defghijklmnopqrstuvwxyz'
>>> s[:]
'abcdefghijklmnopqrstuvwxyz'
>>> print(s)
abcdefghijklmnopqrstuvwxyz
>>> s[3:1000]
'defghijklmnopqrstuvwxyz'
>>> s[5:1]
''
>>> s[5:-1]
'fghijklmnopqrstuvwxy'
>>> s[5:-5]
'fghijklmnopqrstu'
>>> s[-5:5]
''
>>> 