Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dict
>>> #a group of objects as key-value pairs
>>> # rollno-name
>>> # mobilenumber-address
>>> #word:meaning
>>> d={k1:v1,k2:v2,k3=v3}
SyntaxError: invalid syntax
>>> d={k1:v1,k2:v2,k3:v3}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d={k1:v1,k2:v2,k3:v3}
NameError: name 'k1' is not defined
>>> d={10: 'Mohit',20:'ram',30='sita'}
SyntaxError: invalid syntax
>>> d={10: 'Mohit',20:'ram',30:'sita'}
>>> print(type(d))
<class 'dict'>
>>> type(d)
<class 'dict'>
>>> d={}
>>> # d[key]=value
>>> d[10]='mohit'
>>> d[20]='ram'
>>> print(d)
{10: 'mohit', 20: 'ram'}
>>> #duplicate keys are not allowed
>>> d[10]='ram'
>>> print(d)
{10: 'ram', 20: 'ram'}
>>> d={10:'Ram',20:'Ram',30:'Ram'}
>>> print(d)
{10: 'Ram', 20: 'Ram', 30: 'Ram'}
>>> #duplicate keys not #duplicate values allowed
>>> #mutable
>>> 3INDEXING AND SLICING NOT APLLICABLE
SyntaxError: invalid syntax
>>> #INDEXING AND SLICING NOT APLLICABLE
>>> #range
>>> r=range(10)
>>> print(type(r))
<class 'range'>
>>> print(r)
range(0, 10)
>>> for x in r :
	print(x):
		
SyntaxError: invalid syntax
>>> r=range(10)
>>> for x in r :
	
	 print(r);

	
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
>>> for x in r :

	 print(x);

	 
0
1
2
3
4
5
6
7
8
9
>>> #form-1:
>>> # range(n)
>>> #from 0 to n-1
>>> #form-2:
>>> #  range(begin,end)
>>> r=range(1,10)
>>> print(r)
range(1, 10)
>>> fpr x in r :
	
SyntaxError: invalid syntax
>>> for x in r :
	print(x);

	
1
2
3
4
5
6
7
8
9
>>> r=range(1,11)
>>> for x in r :
	print(x);

	
1
2
3
4
5
6
7
8
9
10
>>> #form-3 range(begin,end,increment/decrement)
>>> r=range(1,21,1)
>>> for x in r:
	print(x);

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> r=range(1,21,4)
>>> for x in r:
	print(x);

	
1
5
9
13
17
>>> range(21,1,-5)
range(21, 1, -5)
>>> r=range(21,1,-5)
>>> for x in r :
	print(x)

	
21
16
11
6
>>> r=range(10,21)
>>> print(r[-1])
20
>>> print(r[0])
10
>>> r1=r[1:5]
>>> print(r1)
range(11, 15)
>>> for x in r1 :
	print(x);

	
11
12
13
14
>>> for x in r1 :
	print(x)

	
11
12
13
14
>>> #immutable
>>> r[4]=10000
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    r[4]=10000
TypeError: 'range' object does not support item assignment
>>> #bytes and bytearray
>>> l=[10,20,30,40]
>>> b=bytes(l)
>>> print(type(l))
<class 'list'>
>>> print(type(b))
<class 'bytes'>
>>> for x in b :
	print(x)

	
10
20
30
40
>>> #values only from 0 t0 255
>>> l=[10,20,30,40,256]
>>> b=bytes(l)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    b=bytes(l)
ValueError: bytes must be in range(0, 256)
>>> l=[10,20,30,40]
>>> b=bytes(l)
>>> print(b[0])
10
>>> b[0]=77
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    b[0]=77
TypeError: 'bytes' object does not support item assignment
>>> bytearray:
	
SyntaxError: invalid syntax
>>> #bytearray
>>> l=[10,20,30,40]
>>> b=bytearray(l)
>>> print(b[0]=10)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(b[0])=10)
SyntaxError: unmatched ')'
>>> print(b[0])
10
>>> print(b[-1])
40
>>> print(type(b))
<class 'bytearray'>
>>> # value only from 0 t0 255
>>> l=[10,20,30,40,256]
>>> b=bytearray(l)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    b=bytearray(l)
ValueError: byte must be in range(0, 256)
>>> b[0]=1000
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    b[0]=1000
ValueError: byte must be in range(0, 256)
>>> b[0]=77
>>> for x in b :
	print(x)

	
77
20
30
40
>>> #mutable
>>> 