Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l.append(10)
>>> l.append('durga')
>>> l.append(10)
>>> print(l)
[10, 'durga', 10]
>>> l[0]=77
>>> print(l)
[77, 'durga', 10]
>>> l=list('durga')
>>> print(l)
['d', 'u', 'r', 'g', 'a']
>>> l=list(range(0,10,2))
>>> print(l)
[0, 2, 4, 6, 8]
>>> s='Learning Python is easy'
>>> print(s)
Learning Python is easy
>>> l=s.split()
>>> print(s)
Learning Python is easy
>>> print(l)
['Learning', 'Python', 'is', 'easy']
>>> l=list(range(0,10,2))
>>> print(l)
[0, 2, 4, 6, 8]
>>> l[0]
0
>>> print(type(l[0]))
<class 'int'>
>>> l=[10,20,30,40,50,60,70,80,90,100]
>>> l[2:7]
[30, 40, 50, 60, 70]
>>> l[2:7:2]
[30, 50, 70]
>>> l[4:::2]
SyntaxError: invalid syntax
>>> l[4::2]
[50, 70, 90]
>>> l[8:2:-2]
[90, 70, 50]
>>> l[4:100]
[50, 60, 70, 80, 90, 100]
>>> l[4:0:2]
[]
>>> l[4::1]
[50, 60, 70, 80, 90, 100]
>>> l[::1]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> l[::-1]
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> l1=[10,20,30]
>>> l2=[40,50,60]
>>> l3=l1+l2
>>> print(l3)
[10, 20, 30, 40, 50, 60]
>>> print(l3,l1+l2))
SyntaxError: unmatched ')'
>>> print(l3,l1+l2)
[10, 20, 30, 40, 50, 60] [10, 20, 30, 40, 50, 60]
>>> l1=[10,20,30]
>>> l2=l1+40
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l2=l1+40
TypeError: can only concatenate list (not "int") to list
>>> l2=l1+[40]
>>> print(l2)
[10, 20, 30, 40]
>>> l2=l1+(40,50,60)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l2=l1+(40,50,60)
TypeError: can only concatenate list (not "tuple") to list
>>> l1=[10,20]
>>> l2=l1*2
>>> print(l2)
[10, 20, 10, 20]
>>> l2=2*l1
>>> print(l2)
[10, 20, 10, 20]
>>> l2=2.0*l1
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l2=2.0*l1
TypeError: can't multiply sequence by non-int of type 'float'
>>> l1=[10,20]
>>> l2=[30,40]
>>> l3=l1+l2
>>> l4=l3*3
>>> print(l4)
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
>>> l1=['dog,'cat','Rat']
    
SyntaxError: invalid syntax
>>> l1=['dog,'cat','Rat']
    
SyntaxError: invalid syntax
>>> l1=['Dog','Cat','Rat']
>>> l1=['Dog','Cat','Rat']
>>> 12=['Dog','Cat','Rat']
SyntaxError: cannot assign to literal
>>> 