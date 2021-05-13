Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l.append(10)
>>> l.append(20)
>>> l.append(30)
>>> print(l)
[10, 20, 30]
>>> l.append(40)
>>> l=[10,20,30,40]
>>> l.insert[1,50]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.insert[1,50]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l=[10,20,10,20,40]
>>> l.remove(40)
>>> print(l)
[10, 20, 10, 20]
>>> l.remove(10)
>>> print(l)
[20, 10, 20]
>>> l.remove(50)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.remove(50)
ValueError: list.remove(x): x not in list
>>> l=[10,20,30]
>>> l,pop()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l,pop()
NameError: name 'pop' is not defined
>>> l.pop()
30
>>> print(l)
[10, 20]
>>> print(l.pop())
20
>>> print(l)
[10]
>>> print(l.pop())
10
>>> print(l)
[]
>>> print(l.pop())
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(l.pop())
IndexError: pop from empty list
>>> l=[10,20,30,40]
>>> print(l.pop(l))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(l.pop(l))
TypeError: 'list' object cannot be interpreted as an integer
>>> l.pop(l)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.pop(l)
TypeError: 'list' object cannot be interpreted as an integer
>>> print(l.remove(10))
None
>>> l=[10,20,30,40]
>>> print(l)
[10, 20, 30, 40]
>>> l.reverse()
>>> print(l)
[40, 30, 20, 10]
>>> l=[10,20,30,40]
>>> r=reversed(l)
>>> print(r)
<list_reverseiterator object at 0x0000020A841981F0>
>>> l1=list(r)
>>> print(l1)
[40, 30, 20, 10]
>>> print(type(r))
<class 'list_reverseiterator'>
>>> print(l)
[10, 20, 30, 40]
>>> s='durga'
>>> s.reverse()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> r=reversed(s)
>>> for x in r:
	print(x)

	
a
g
r
u
d
>>> l1=[10,20,30,40]
>>> l2=l1
>>> l1[1]=7777
>>> print(l1)
[10, 7777, 30, 40]
>>> print(l2)
[10, 7777, 30, 40]
>>> print(id(l1))
2244189447744
>>> print(id(l2))
2244189447744
>>> l1 is l2
True
>>> l1=[10,20,30,40]
>>> l2=l1[::]
>>> print(id(l1))
2244189136768
>>> print(id(l2))
2244189225728
>>> l1[1]=7777
>>> l2
[10, 20, 30, 40]
>>> l1=[10,20,30,40]
>>> l2=l1.copy()
>>> l2
[10, 20, 30, 40]
>>> l1[1]=7777
>>> print(l1)
[10, 7777, 30, 40]
>>> print(l2)
[10, 20, 30, 40]
>>> 