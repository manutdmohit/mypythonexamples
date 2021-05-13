Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operators
>>> Arithmetic Operators
SyntaxError: invalid syntax
>>> #Arithmetic operators
>>> Arithmetic operators
SyntaxError: invalid syntax
>>> #Arithmetic operators
>>> # =,-,*,/,%,// = Floor Divison Operator    ** = Exponential Operator/ Power Operator
>>> print(10/2)
5.0
>>> #ALWAYS FLOATING VALUE
>>> print(10/3)
3.3333333333333335
>>> # / =floating point value    # //= Floor division operator -- integral and floating point airthmetic
>>> print(10//2)
5
>>> print(10.0/2)
5.0
>>> print(10.0//2)
5.0
>>>  print(10/3)
 
SyntaxError: unexpected indent
>>> print(10/3)
3.3333333333333335
>>> print(10.0/3)
3.3333333333333335
>>> print(10//3)
3
>>> print(10.0//3)
3.0
>>> 20/2
10.0
>>> 20.5/2
10.25
>>> 20//2
10
>>> 20.5//2
10.0
>>> 30//2
15
>>> primt(10**2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    primt(10**2)
NameError: name 'primt' is not defined
>>> print(10**2)
100
>>> print(3**3)
27
>>> 10+20
30
>>> 'ram' + 'sita'
'ramsita'
>>> # concatenation
>>> 'ram' + 10
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'ram' + 10
TypeError: can only concatenate str (not "int") to str
>>> 'durga' + '10"
SyntaxError: EOL while scanning string literal
>>> 'durga' + '10'
'durga10'
>>> 'durga + str(10)
SyntaxError: EOL while scanning string literal
>>> 'durg'a + str(10)
SyntaxError: invalid syntax
>>> 'durga' + str(10)
'durga10'
>>> print('durga' + str(10))
durga10
>>> print('ram'*3)
ramramram
>>> print(3*'ram')
ramramram
>>> print('ram' * 'sita')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print('ram' * 'sita')
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('durga' * '3')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print('durga' * '3')
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('durga' * int('3'))
durgadurgadurga
>>> # + for string (concatenation)  str+str
>>> # for string       string multiplication operator and string repetition operator
>>> # string * int
>>> # int * string
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> 10.0//0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    10.0//0
ZeroDivisionError: float divmod()
>>> float divmod(10/0)
SyntaxError: invalid syntax
>>> print('ram' * True)
ram
>>> print('ram' * False)

>>> #relational operators
>>> # >, >=, <, <=
>>> a=10
>>> b=20
>>> print(a<b)
True
>>> print(a<=b)
True
>>> print(a>b)
False
>>> print(a>=b)
False
>>> ord('a)
    
SyntaxError: EOL while scanning string literal
>>> ord('a')
97
>>> ord('A')
65
>>> chr(97)
'a'
>>> print(chr('A'))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(chr('A'))
TypeError: an integer is required (got type str)
>>> print(ord('A'))
65
>>> print(chr('122'))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(chr('122'))
TypeError: an integer is required (got type str)
>>> print(chr('112'))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(chr('112'))
TypeError: an integer is required (got type str)
>>> print(chr(98))
b
>>> print(chr(122))
z
>>> s='ram'
>>> s2='sita'
>>> print(s1<s2)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(s1<s2)
NameError: name 's1' is not defined
>>> s1='ram'
>>> print(s1<s2)
True
>>> print(s1<=s2)
True
>>> print(s1>s2)
False
>>> print(s1>=s2)
False
>>> s1='ram'
>>> s2='ram'
>>> print(s1<s2)
False
>>> print(s1<=s2)
True
>>> print(s1>=s2)
True
>>> print(s1>s2)
False
>>> s1='ram'
>>> s1='Ram'
>>> print(s1<s2)
True
>>> print(s1<=s2)
True
>>> print(s1>=s2)
False
>>> print(s1>s2)
False
>>> s2='Ram'
>>> print(s1<s2)
False
>>> print(s1<=s2)
True
>>> print(s1>s2)
False
>>> print(s1>=s2)
True
>>> print(True > False)
True
>>> print(True >= False)
True
>>> print(True < False)
False
>>> print(True <= False)
False
>>> print(10<'ram')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(10<'ram')
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a=10
b=20
>>> a=10
>>> b=20
>>> if a>b :
	print('a is greater than b')
	else :
		
SyntaxError: invalid syntax
>>> if a>b :
	print('a is greater than b')
	else:
		
SyntaxError: invalid syntax
>>> if a>b :
	print('a is greater than b')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a>b :
	print('a is greater than b')
    else :
	    
SyntaxError: unindent does not match any outer indentation level
>>> 10<20
True
>>> 10<20<30
True
>>> 10<20<30<40
True
>>> 10<20<30<40>50
False
>>> #equality operators
>>> # ==, !=
>>> 10==20
False
>>> 10!=20
True
>>> 1== True
True
>>> 1== False
False
>>> 10==10.0
True
>>> 
>>> 'ram' =='ram'
True
>>> 10 =='durga'
False
>>> 10=='durga'
False
>>> 10=='10'
False
>>> 10==20==30==40
False
>>> 10=20
SyntaxError: cannot assign to literal
>>> 10==10==10==10
True
>>> is     #reference comparison or address comparison
SyntaxError: invalid syntax
>>> # is     #reference comparison or address comparison
>>> # == given
>>> l1=[10,20,30]
>>> l2=[10,20,30]
>>> print(l1 is l2)
False
>>> print(l1==l2)
True
>>> print(id(l1))
2742051564928
>>> print(id(l2))
2742051628224
>>> l3=l1
>>> print(l1 is l3)
True
>>> 