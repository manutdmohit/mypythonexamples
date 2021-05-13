Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1={10,20,30}
>>> s2={40+50+60}
>>> s1+s2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1*s2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s1*s2
TypeError: unsupported operand type(s) for *: 'set' and 'set'
>>> s1*3
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> 3*s1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    3*s1
TypeError: unsupported operand type(s) for *: 'int' and 'set'
>>> s2={40+50+60}
>>> s1+s2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s2={40,50,60}
>>> s1+s2
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1={10,20,30}
>>> s2={30,10,20}
>>> print(s1==s2)
True
>>> print(s1!=s2)
False
>>> s1={10,20,30}
>>> s2={20,10,5,6,6}
>>> s1<s2
False
>>> s1>s2
False
>>> s1<=s2
False
>>> s1>=s2
False
>>> s1={10,20,30,40}
>>> 10 in s1
True
>>> 50 in s1
False
>>> 50 not in s1
True
>>> s={10,20,30,40}
>>> len(s)
4
>>> s={10,20,30,40}
>>> s.add(50)
>>> print(s)
{40, 10, 50, 20, 30}
>>> s={10,20,30,40}
>>> s.remove(30)
>>> print(s)
{40, 10, 20}
>>> s.remove(50)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.remove(50)
KeyError: 50
>>> s={10,20,30,40}
>>> s.discard(30)
>>> print(s)
{40, 10, 20}
>>> s.discard(50)
>>> print(s)
{40, 10, 20}
>>> s={10,20,30,40}
>>> print(s.pop())
40
>>> print(s.pop())
10
>>> print(s.pop())
20
>>> print(s.pop())
30
>>> print(s.pop())
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(s.pop())
KeyError: 'pop from an empty set'
>>> print(s)
set()
>>> s={10,20,30,40}
>>> s.clear()
>>> print(s)
set()
>>> s1={10,20,30}
>>> s2=s1
>>> print(id(s1))
2041902837312
>>> print(id(s2))
2041902837312
>>> s2=s1.copy()
>>> print(id(s1))
2041902837312
>>> print(id(s2))
2041902836416
>>> s1.pop()
10
>>> print(s2)
{10, 20, 30}
>>> print(s1)
{20, 30}
>>> s1={10,20,30}
>>> s2=s1
>>> s1.pop()
10
>>> print(s1)
{20, 30}
>>> print(s2)
{20, 30}
>>> s1={10,20,30}
>>> s2=s1.copy()
>>> s1.pop()
10
>>> print(s1)
{20, 30}
>>> print(s2)
{10, 20, 30}
>>> l=[10,10,20,30,10,20,30]
>>> l1=[]
>>> for x in l:
	if x not in l1:
		l1.append(x)

		
>>> print(l1)
[10, 20, 30]
>>>   l={10,10,20,30,10,20,30}
  
SyntaxError: unexpected indent
>>> l={10,10,20,30,10,20,30}
>>> s={10,10,20,30,10,20,30}
>>> s1=[]
>>> for x in sl:
	if x not in s1:
		l1.append(x)

		
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    for x in sl:
NameError: name 'sl' is not defined
>>> s1=()
>>> s1={}
>>> for x in sl:
	if x not in s1:
		l1.append(x)

		
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    for x in sl:
NameError: name 'sl' is not defined
>>> s1={,}
SyntaxError: invalid syntax
>>> s1=set()
>>> for x in sl:
	if x not in s1:
		l1.append(x)

		
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    for x in sl:
NameError: name 'sl' is not defined
>>> s={10,10,20,30,10,20,30}
>>> s1=set()
>>> for x in sl:
	if x not in s1:
		s1.append(x)

		
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for x in sl:
NameError: name 'sl' is not defined
>>> d={100:'durga','A':300,200:'Ravi','B':400}
>>> d={100:'durga','A':300,200:'Ravi','B':400,100:'Ram'}
>>> print(d)
{100: 'Ram', 'A': 300, 200: 'Ravi', 'B': 400}
>>> l=[(100,'A'),(200,'B',(300,'C')]
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> l=[(100,'A'),(200,'B'),(300,'C')]
>>> d=dict(l)
>>> print(l)
[(100, 'A'), (200, 'B'), (300, 'C')]
>>> print(d)
{100: 'A', 200: 'B', 300: 'C'}
>>>  d=eval(input('Enter any dictionary'))
 
SyntaxError: unexpected indent
>>> d=eval(input('Enter any dictionary'))
Enter any dictionary{100:'durga',200:'ram',300:'sita'}
>>> print(d)
{100: 'durga', 200: 'ram', 300: 'sita'}
>>> d={100: 'durga', 200: 'ram', 300: 'sita'}
>>> d[100]
'durga'
>>> d[300]
'sita'
>>> d[200]
'ram'
>>> d[700]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    d[700]
KeyError: 700
>>> key=int(input('Enter key to find value'))
Enter key to find value100
>>> 