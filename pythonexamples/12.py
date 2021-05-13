Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #collection Related Data Types:
>>> #list tuple set frozenset dict range bytes bytearray
>>> #list
>>> l=[10,'durga',20,10,10]     #duplicates are allowed
>>> print(type(l))
<class 'list'>
>>> print(l)
[10, 'durga', 20, 10, 10]
>>> #order is important
>>> #order preserved
>>> #duplicate objects are allowed
>>> [  ]
[]
>>> #[  ]
>>> #hetrogenous objects are allowed
>>> print(l[0])
10
>>> l=[10,'durga',20,10,30]
>>> print(l[-1])
30
>>> print(l[1:4])
['durga', 20, 10]
>>> #indexing and slicing are allowed
>>> l=[ ]
>>> l.append(10)     #append()
>>> l.append(20)
>>> l.append(30)
>>> l.append(40)
>>> print(l[])
SyntaxError: invalid syntax
>>> print(l)
[10, 20, 30, 40]
>>> l.remove(30) #remove()
>>> print(l)
[10, 20, 40]
>>> #list is growable in nature
>>> l[0]=7777
>>> print(l)
[7777, 20, 40]
>>> # mutable
>>> #Tuple
>>> #exactly same as list except that it is       #immutable
>>> *read only version of list
SyntaxError: invalid syntax
>>> #read only version of list
>>> t=(10,20,30,10,'ram')
>>> print(type(t))
<class 'tuple'>
>>> print(t[0])
10
>>> print(t[-1])
ram
>>> print(t[1:4])
(20, 30, 10)
>>> t[0]=7777
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t[0]=7777
TypeError: 'tuple' object does not support item assignment
>>> t.append(50)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t.append(50)
AttributeError: 'tuple' object has no attribute 'append'
>>> t.remocve()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t.remocve()
AttributeError: 'tuple' object has no attribute 'remocve'
>>> t.remove(10)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.remove(10)
AttributeError: 'tuple' object has no attribute 'remove'
>>> t=( )
>>> print(type(t))
<class 'tuple'>
>>> print(type(t))
<class 'tuple'>
>>> print(type(t))   #false
<class 'tuple'>
>>> print(type(t))   #ok
<class 'tuple'>
>>> t=(10)
>>> print(type(t))
<class 'int'>
>>> t=(10,)
>>> print(type(t))
<class 'tuple'>
>>> #immutable, ( ), requires less moemory, Faster Access(performance is more)
>>> #set data type
>>> #duplciates are not allowes
>>> #order not required
>>> s={10,20030,40}
>>> print(type(s))
<class 'set'>
>>> s={10,20,30,40}
>>> print(type(s))
<class 'set'>
>>> s={10,20,30,30}
>>> print(type(s))
<class 'set'>
>>> print(s)
{10, 20, 30}
>>> s={10,20,;'ram',40,10,11}
SyntaxError: invalid syntax
>>> s={10,20,,'ram',40,10,11}
SyntaxError: invalid syntax
>>> s={10,20,'ram',40,10,11}
>>> print(s)
{40, 10, 11, 'ram', 20}
>>> print(s[0])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(s[0])
TypeError: 'set' object is not subscriptable
>>> 
>>> print(s[1:4)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(s[1:4))
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(s[1:4])
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(s[1:4])
TypeError: 'set' object is not subscriptable
>>> #inde#duplciates are not allowed #order not required
>>> #hetrogenous allowed
>>> s={10.20,30,40}
>>> s.add(50)
>>> print(s)
{40, 10.2, 50, 30}
>>> s.remove(30)
>>> print(s)
{40, 10.2, 50}
>>> #growable and mutable
>>> #append() vs add()
>>> s=[10,20,30,40]
>>> s.append(50)
>>> print(s)        #append last
[10, 20, 30, 40, 50]
>>> s={10,20,30,40}s.append(50)
SyntaxError: invalid syntax
>>> s=[10,20,30,40]
>>> s={10,20,30,40}
>>> s.add(50)
>>> print(s)
{40, 10, 50, 20, 30}
>>> s={ }            #dict
>>> print(type(s))
<class 'dict'>
>>> s=set()
>>> print(type(s))
<class 'set'>
>>> 