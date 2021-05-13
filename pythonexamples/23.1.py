Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='ABCABCABCA'
>>> print(s.count('ABC'))
3
>>> i=s.find('ABC')
>>> print(i)
0
>>> i=s.find('ABC',3,10)
>>> print(i)
3
>>> i=s.find('ABC',6,10)
>>> print(i)
6
>>> 
>>> i=s.find('ABC',9,10)
>>> print(i)
-1
>>> i=s.count('ABC')
>>> print(i)
3
>>> 