Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> type(s)
<class 'set'>
>>> s.add(10)
>>> s.add('Z')
>>> s.add('A')
>>> s.add('20')
>>> s.add('10')
>>> print(s)
{'A', '10', 10, 'Z', '20'}
>>>  s[0]
 
SyntaxError: unexpected indent
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[1:3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[1:3]
TypeError: 'set' object is not subscriptable
>>> 19+7/60
19.116666666666667
>>> 19+9+10+8+11+11+7+17+12+6+28+11+6+14
169
>>> 169+(17+2+47+33+10+57+47+16+4+23+21+38+16+58)/60
175.48333333333332
>>> 175.48333333333332+10+24/60
185.88333333333333
>>> l={10,20,30,40}
>>> s=set(l)
>>> print(s)
{40, 10, 20, 30}
>>> l=[10,20,30,40]
>>> s=set(l)
>>> print(s)
{40, 10, 20, 30}
>>> s=set(range(0,101,10))
>>> print(s)
{0, 100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
>>> s=set('apple)
      
SyntaxError: EOL while scanning string literal
>>> s=set('apple')
>>> print(s)
{'p', 'l', 'e', 'a'}
>>> s=eval(input('Enter set of values'))
Enter set of values{10,20,30,40}
>>> print(s)
{40, 10, 20, 30}
>>> 