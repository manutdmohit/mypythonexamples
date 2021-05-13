Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #logical operators for boolean
>>> #  and ,or ,not
>>> # for boolean types    # and= returns True if both arguments True
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> False and True
False
>>> # or = returns true iff atleast one argument is true
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> False or True
True
>>> print(True and True)
True
>>> print(True and False)
False
>>> print(False and False)
False
>>> print(False and True)
False
>>> print(True or True)
True
>>> print(True or False)
True
>>> print(False or True)
True
>>> print(False or False)
False
>>> # not = complement
>>> not True = False
SyntaxError: cannot assign to operator
>>> not False= True
SyntaxError: cannot assign to operator
>>> #not True = False
>>> #not False= True
>>> not True
False
>>> not False= True
SyntaxError: cannot assign to operator
>>> not False= True
SyntaxError: cannot assign to operator
>>> not False
True
>>> username=input('Enter username:')
Enter username:sdsd
>>> #logical operators for non-boolean types
>>> str=bool(' ')
>>> print(str)
True
>>> str=bool('')
>>> print(str)
False
>>> s={1,2,3,4}
>>> print(s)
{1, 2, 3, 4}
>>> s[0]=100
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s[0]=100
TypeError: 'set' object does not support item assignment
>>> 
>>> # x and y = result is x|y
>>> # if x evaluates to False, then result is x
>>> # if x evaluates to True, then result is y
>>> 10 and 20
20
>>> 0 and 20
0
>>>  .ram' and 'sita'
 
SyntaxError: unexpected indent
>>> 'ram' and 'sita'
'sita'
>>> '' and 'sita'
''
>>> # x or y
>>> 10 or 20
10
>>> 0 or 20
20
>>> 10 or 0
10
>>>  0 or 0
 
SyntaxError: unexpected indent
>>> 0 or 0
0
>>> 10 and 0
0
>>> [] or 'durga'
'durga'
>>> 'ram' or 'durga'
'ram'
>>> '' or 'durga'
'durga'
>>> '' or []
[]
>>> '' or ''
''
>>> not 1
False
>>> not 0
True
>>> not []
True
>>> not ''
True
>>> not ' '
False
>>> not 'ram'
False
>>> not 'durga'
False
>>> not 0
True
>>> not 10
False
>>> #bitwise operators
>>> & - biwise and
SyntaxError: invalid syntax
>>> #& - biwise and
>>> #| - biwise or
>>> #^ - bitwise x-or
>>> #~ - bitwise complement
>>> #<< - bitwise left-shift
>>> #>> - bitwise right-shift
>>> 4 & 5
4
>>> # only for int and bool type
>>> 10.5 & 20.6
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    10.5 & 20.6
TypeError: unsupported operand type(s) for &: 'float' and 'float'
>>> 'ram' & 'ram'
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    'ram' & 'ram'
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> & = if both bits are 1 then result is 1 other wise 0
SyntaxError: invalid syntax
>>> #& = if both bits are 1 then result is 1 other wise 0
>>> #& = if atleast one bit is 1 then result is 1 other wise 0
>>> # ^ = if both bits are differen 1 else 0
>>> 11 ^ 22
29
>>> 11 ^ 11
0
>>> 11 & 0
0
>>> #| = if atleast one bit is 1 then result is 1 other wise 0
>>> 
>>> ~11
-12
>>> ~122
-123
>>> print(4 & 5)
4
>>> print(4 | 5)
5
>>> print(4 ^ 5)
1
>>> print(~4)
-5
>>> # the most significant bit(MSB) acts as sign bit
>>> # 0 = +ve number
>>> # 1 = - -ve number
>>> # +ve numbers will be represented directed in the memory
>>> # -ve numbers will be represented in 2's complement form
>>> # 1's complement    0=1 and 1= 0
>>> # 2's complement    1's complement + 1
>>>  # 32-bit representation
 
>>>  print(~-4)
 
SyntaxError: unexpected indent
>>> print(~-4)
3
>>> print(~5)
-6
>>> #shift operators
>>> # << = left shift
>>> # >> = right shift
>>> 10 <<2
40
>>> 20<<2
80
>>> 20<<2-
SyntaxError: invalid syntax
>>> 20<<-2
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    20<<-2
ValueError: negative shift count
>>> 10..2
SyntaxError: invalid syntax
>>> 10>>2
2
>>> 10 | 20
30
>>> ~True
-2
>>> `-2
SyntaxError: invalid syntax
>>> ~-2
1
>>> ~1
-2
>>> True<<2
4
>>> True>>2
0
>>> #assignment operators
>>> x=10
>>> x+=20
>>> print(x)
30
>>> # +=compound assignment operator
>>> x=10
>>> x &=5
>>> print(x)
0
>>> x ^=5
>>> print(x)
5
>>>  x=10
 
SyntaxError: unexpected indent
>>> x=10
>>> x^=5
>>> prin(x)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    prin(x)
NameError: name 'prin' is not defined
>>> print(x)
15
>>> x=10
>>> x **=2
>>> print(x)
100
>>> x=10
>>> x++
SyntaxError: invalid syntax
>>> x=10
>>> x--
SyntaxError: invalid syntax
>>> x=10
>>> x-
SyntaxError: invalid syntax
>>> x=10
>>> print(++x)
10
>>> print(++++x)
10
>>> print(-x)
-10
>>> print(--x)
10
>>> #ternanry operator
>>> 3 - Ternanry operator
SyntaxError: invalid syntax
>>> 
>>> #3 - Ternanry operator
>>> a=10
>>> b=20
>>> c= 30 if a>b else 40
>>> #syntax
>>> #    c=first_value if condition else second-value
>>> c= 30 if a>b else 40
>>> print(c)
40
>>> a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
min= a if a<b else b
print('The minimum vlaue :', min)
SyntaxError: multiple statements found while compiling a single statement
>>> a=int(input('Enter first number : ')
b=int(input('Enter second number : ')
min= a if a<b else b
print('The minimum vlaue :', min)
      
SyntaxError: invalid syntax
>>> # nesting of to is possible
>>> 