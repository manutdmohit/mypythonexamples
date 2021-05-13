Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= True
>>> b= True
>>> print(a is b)
True
>>> a='Ram'
>>> b='Ram'
>>> print(a is b)
True
>>> a=10+20j
>>> b=10+20j
>>> print(a is b)
False
>>> #complex is ....
>>> a is b
False
>>> #mutability
>>> l=[10,20,30]
>>> print(id(l))
1941012149376
>>> l[0]=[7777}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l[0]=[7777]
>>> print(l)
[[7777], 20, 30]
>>> print(id(l))
1941012149376
>>> #changes in existing object#
>>> 
>>> l1=[10,20,30,40]
>>> l2=l1
>>> print(l1)
[10, 20, 30, 40]
>>> print(l2)
[10, 20, 30, 40]
>>> l1[0]=7777
>>> print[l1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print[l1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(l1)
[7777, 20, 30, 40]
>>> print(l2)
[7777, 20, 30, 40]
>>> print(id(l1))
1941012083392
>>> print(id(l2))
1941012083392
>>> l2[1]=11212
>>> print(l1)
[7777, 11212, 30, 40]
>>> print(l2)
[7777, 11212, 30, 40]
>>> 