Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #mutable
>>> #immutable
>>> x=10
>>> print(id(x))
140726969374656
>>> x=x+1
>>> print(id(x))
140726969374688
>>> x
11
>>> print(x)
11
>>> x=10
>>> y=x
>>> print(id(x))
140726969374656
>>> print(id(y))
140726969374656
>>> y=y+1
>>> print(id(y))
140726969374688
>>> print(x)
10
>>> print(y)
11
>>> a=10
>>> b-10
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b-10
NameError: name 'b' is not defined
>>> b=10
>>> c=10
>>> print(id(a))
140726969374656
>>> print(id(b))
140726969374656
>>> print(id(c))
140726969374656
>>> #That was memory utilization, Performance better
>>> a=1000.234
>>> b=1000.234
>>> print(a is b)
False
>>>   a=1000.234
  
SyntaxError: unexpected indent
>>> a=1000.234
>>> b=1000.234
>>> print(a is b)
False
>>> 
================================ RESTART: Shell ================================
>>> b=1000.234
>>> 
>>> a=1000.234
>>> print(a is b)
False
>>> 