Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(10,'durga'20,10)
SyntaxError: invalid syntax
>>> t=(10,'durga',20,10)
>>> t=10,'durga',20,10
>>> print(type(t))
<class 'tuple'>
>>> print(t)
(10, 'durga', 20, 10)
>>> t[0]
10
>>> t[1]
'durga'
>>> t[2]
20
>>> t[3]
10
>>> t[4]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
>>> t[0]=100
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t[0]=100
TypeError: 'tuple' object does not support item assignment
>>> t[-1]
10
>>> t[-2]
20
>>> t[-3]
'durga'
>>> t[-4]
10
>>> t=(10,20,40)
>>> t=(10,20)
>>> t(10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t(10)
TypeError: 'tuple' object is not callable
>>> t=(10)
>>> print(type(t))
<class 'int'>
>>> t=(10,)
>>> print(type(t))
<class 'tuple'>
>>> t=()
>>> t=(10)
>>> print(type(t))
<class 'int'>
>>> t=()
>>> print(type(t))
<class 'tuple'>
>>> t=(10,)
>>> print(type(t))
<class 'tuple'>
>>> t=10
>>> print(type(t))
<class 'int'>
>>> t=(10,20,30)
>>> print(type(t))
<class 'tuple'>
>>> t=10,20,30
>>> print(type(t))
<class 'tuple'>
>>> t=10,
>>> print(type(t))
<class 'tuple'>
>>> t=(10,20,30,)
>>> print(type(t))
<class 'tuple'>
>>> t=10,20,30,
>>> print(type(t))
<class 'tuple'>
>>> l=[10,20,30]
>>> t=tuple(l)
>>> print(t)
(10, 20, 30)
>>> t=tuple(range(1,11,2))
>>> print(t)
(1, 3, 5, 7, 9)
>>> t=tuple('durgA')
>>> t=tuple('durga')
>>> print(t)
('d', 'u', 'r', 'g', 'a')

>>> t=eval(input('Enter Tuple of Values:'))
Enter Tuple of Values:{1,2,3,4}
>>> print(t)
{1, 2, 3, 4}
>>> t=eval(input('Enter Tuple of Values:'))
Enter Tuple of Values:1 2 3 4
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    t=eval(input('Enter Tuple of Values:'))
  File "<string>", line 1
    1 2 3 4
      ^
SyntaxError: invalid syntax
>>> t=(10,20,30,40)
>>> t[0]
10
>>> t[-1]
40
>>> t[100]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    t[100]
IndexError: tuple index out of range
>>> t=(10,20,30,40,50,60,70,80)
>>> t[2:5]
(30, 40, 50)
>>> t[::2]
(10, 30, 50, 70)
>>> t1=(10,20,30)
>>> t2=(40,50,60)
>>> t1+t2
(10, 20, 30, 40, 50, 60)
>>> t1=(10,20,30)
>>> t2=t1*3
>>> print(t2)
(10, 20, 30, 10, 20, 30, 10, 20, 30)
>>> t1=(10,20,30)
>>> t2=(40,50,60)
>>> t3=t1+10
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    t3=t1+10
TypeError: can only concatenate tuple (not "int") to tuple
>>> t3=t1+[10,20]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    t3=t1+[10,20]
TypeError: can only concatenate tuple (not "list") to tuple
>>> t1=(10,20,30)
>>> t2=t1*3
>>> print(t2)
(10, 20, 30, 10, 20, 30, 10, 20, 30)
>>> t1=(10,20)
>>> t2=(30,40)
>>> t3=t1+t2
>>> t4+t3*3
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t4+t3*3
NameError: name 't4' is not defined
>>> t4=t3*3
>>> print(t4)
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)
>>> t1=('Cat','Rat','Dog')
>>> t2=('Cat','Rat','Dog')
>>> t3=('CAT','RAT','DOG')
>>> t4=('Rat','Dog','Cat')
>>> t1==t2
True
>>> t1==t3
False
>>> t1==t4
False
>>> t1<t2
False
>>> t1<=t2
True
>>> t1=(10,20,30)
>>> t2=(30,15,40)
>>> t1<=t2
True
>>> t1<t2
True
>>> t1<=t2
True
>>> t1>t2
False
>>> t1>=t2
False
>>> t1=(10,20,30)
>>> t2=(10,5,70)
>>> t1<t2
False
>>> t1>t2
True
>>> t1<=t2
False
>>> t1=(10,20,30)
>>> t2=(10,20,30,40,50)
>>> t1<t2
True
>>> t2=(10,20,30)
>>> 10 in t
True
>>> 50 not in t
False
>>>   50 not in t
  
SyntaxError: unexpected indent
>>> 50 not in t
False
>>> 60 not in t
False
>>> 50 not in t
False
>>> 50 in t
True
>>> t1=(10,20,30,40)
>>> print(len(t1))
4
>>> len(t1)
4
>>> 1.count(10)
SyntaxError: invalid syntax
>>> t1.count(10)
1
>>> t=(1,1,2,2,2,3,3)
>>> t1.count(1)
0
>>> t.count(1)
2
>>> t.count(7)
0
>>> t.index(1)
0
>>> t.index(2)
2
>>> t.index(3)
5
>>>  t.index(40)
 
SyntaxError: unexpected indent
>>> t.index(40)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    t.index(40)
ValueError: tuple.index(x): x not in tuple
>>> t=(10,20,30,40)
>>> r=reversed(t)
>>> r
<reversed object at 0x0000026817457250>
>>> print(r)
<reversed object at 0x0000026817457250>
>>> t1=tuple(r)
>>> print(t1)
(40, 30, 20, 10)
>>> print(type())
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    print(type())
TypeError: type() takes 1 or 3 arguments
>>> print(type(r))
<class 'reversed'>
>>> print(type(t))
<class 'tuple'>
>>> t=(20,5,10,15,0)
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> s=sorted(t)
>>> t1=tuple(s)
>>> print(t1)
(0, 5, 10, 15, 20)
>>> t1(;;-1)
SyntaxError: invalid syntax
>>> t1(::-1)
SyntaxError: invalid syntax
>>> t1(::-1)
SyntaxError: invalid syntax
>>> t2=t1(::-1)
SyntaxError: invalid syntax
>>> t1[::-1]
(20, 15, 10, 5, 0)
>>> s=sorted(t,reverse=True)
>>> t1=tuple(s)
>>> t1
(20, 15, 10, 5, 0)
>>> t=(20,5,10,15,0)
>>> max(t)
20
>>> min(t)
0
>>> a=10
>>> b=20
>>> c=30
>>> d=40
>>> t=a,b,c,d
>>> print(t)
(10, 20, 30, 40)
>>> l=[a,b,c,d]
>>> print(t)
(10, 20, 30, 40)
>>> print(l)
[10, 20, 30, 40]
>>> t=(10,20,30,40)
>>> a,b,c,d=t
>>> print(a,b,c,d)
10 20 30 40
>>> t=(10,20,30,40)
>>> a,b,c=t
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3)
>>> a,b=t
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    a,b=t
ValueError: too many values to unpack (expected 2)
>>> a,*b=t
>>> a
10
>>> b
[20, 30, 40]
>>> l=[10,20,30,40]
>>> t=(10,20,30,40)
>>> print(isinstance(l,collection.hashable))
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    print(isinstance(l,collection.hashable))
NameError: name 'collection' is not defined
>>> print(isinstance(l,collections.hashable))
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    print(isinstance(l,collections.hashable))
NameError: name 'collections' is not defined
>>> print(isinstance(l,collections.Hashable))
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    print(isinstance(l,collections.Hashable))
NameError: name 'collections' is not defined
>>> s={10,20}
>>> l=[10,20,30]
>>> t=(10,20,30)
>>> s.add(t)
>>> print(s)
{10, 20, (10, 20, 30)}
>>> s.add(l)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    s.add(l)
TypeError: unhashable type: 'list'
>>> d={}
>>> s[t]='A'
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    s[t]='A'
TypeError: 'set' object does not support item assignment
>>> d[t]='A'
>>> print(d)
{(10, 20, 30): 'A'}
>>> d[l]='A'
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    d[l]='A'
TypeError: unhashable type: 'list'
>>> 