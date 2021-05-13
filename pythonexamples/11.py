Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> s='ram'
>>> output=s[0].upper()+s[1:]
>>> print('output')
output
>>> print(output)
Ram
>>> output=s[0:len(s)-1]+s[-1].upper()
>>> print(output)
raM
>>> s='krishna'
>>> output=s[0].upper+s[1:len[s]-1]+s[-1].upper()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    output=s[0].upper+s[1:len[s]-1]+s[-1].upper()
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> output=s[0].upper()+s[1:len[s]-1]+s[-1].upper()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    output=s[0].upper()+s[1:len[s]-1]+s[-1].upper()
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> output=s[0].upper()+s[1:len(s)-1]+s[-1].upper()
>>> print(output)
KrishnA
>>>   s='krishna'
  
SyntaxError: unexpected indent
>>> s='krishna'
>>> output=s[0]+s[-1+len(s)-1].upper()+s[-1]
>>> print(output)
kNa
>>> output=s[0]+s[1+len(s)-1].upper()+s[-1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    output=s[0]+s[1+len(s)-1].upper()+s[-1]
IndexError: string index out of range
>>> output=s[0]+s[1:len(s)-1].upper()+s[-1]
>>> print(output)
kRISHNa
>>> output
'kRISHNa'
>>> # +operator
>>> s='ram'+'sita'
>>> print(s)
ramsita
>>> s='ram' +10
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s='ram' +10
TypeError: can only concatenate str (not "int") to str
>>> s='ram'+10
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s='ram'+10
TypeError: can only concatenate str (not "int") to str
>>> # *operator
>>> s='durga' *3
>>> print(s)
durgadurgadurga
>>> s='ram'*100
>>> print(s)
ramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramram
>>> s=3 * 'ram'
>>> print(s)
ramramram
>>> s='ram" * 'sita'
SyntaxError: invalid syntax
>>> s='ram' * 'sita'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s='ram' * 'sita'
TypeError: can't multiply sequence by non-int of type 'str'
>>> s=1000 * 1000
>>> print(s)
1000000
>>> s
1000000
>>> #
>>> # Fundamental data types : int,float, complex, bool, str
>>> # long only in python-2
>>> # no char data types and can be represented by str type only
>>> #### Type Casting
>>> #converting type
>>> #### Type Casting or Type coersion
>>> # int() float() complex() bool() str()
>>> #int()
>>> int(10.989)
10
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(3+4j)
TypeError: can't convert complex to int
>>> int(True)
1
>>> int(False)
0
>>> #string internally contains only integral value and base-10
>>> int('15')
15
>>> int('0B111')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int('0B111')
ValueError: invalid literal for int() with base 10: '0B111'
>>> int('10.5')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int('10.5')
ValueError: invalid literal for int() with base 10: '10.5'
>>> #float()
>>> float(10)
10.0
>>> float(0b1111)
15.0
>>> float(0xFace)
64206.0
>>> float(True)
1.0
>>> float(False)
0.0
>>> float(12+13j)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(12+13j)
TypeError: can't convert complex to float
>>> float('111')
111.0
>>> float('Ram')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float('Ram')
ValueError: could not convert string to float: 'Ram'
>>> float(20.04)
20.04
>>> float('20.04)
      
SyntaxError: EOL while scanning string literal
>>> float('20.04')
20.04
>>> float('0xface')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float('0xface')
ValueError: could not convert string to float: '0xface'
>>> #compex()
>>> #complex()
>>> complex(11)
(11+0j)
>>> complex(11.0232)
(11.0232+0j)
>>> complex(2,3)
(2+3j)
>>> complez(0B1111)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    complez(0B1111)
NameError: name 'complez' is not defined
>>> complex(0B1111)
(15+0j)
>>> complex(True)
(1+0j)
>>> Complex(False)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    Complex(False)
NameError: name 'Complex' is not defined
>>> complex(False)
0j
>>> complex('Ram')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    complex('Ram')
ValueError: complex() arg is a malformed string
>>> complex('11111')
(11111+0j)
>>> complex('10.5)
	
SyntaxError: EOL while scanning string literal
>>> complex('10.5')
(10.5+0j)
>>> complex(1.6,2.6)
(1.6+2.6j)
>>> complex('10', '20')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    complex('10', '20')
TypeError: complex() can't take second arg if first is a string
>>> complex(10,'20')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    complex(10,'20')
TypeError: complex() second arg can't be a string
>>> complex('10',20)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    complex('10',20)
TypeError: complex() can't take second arg if first is a string
>>> #bool()
>>> bool(20)
True
>>> bool(10.50)
True
>>> bool(0)
False
>>> bool(-0)
False
>>> bool(20.5)
True
>>> bool(0.0)
False
>>> bool(0.1)
True
>>> bool(0,0)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    bool(0,0)
TypeError: bool expected at most 1 argument, got 2
>>> bool(0+0j)
False
>>> bool(1+0j)
True
>>> bool('True')
True
>>> bool(True')
     
SyntaxError: EOL while scanning string literal
>>> bool('False')
True
>>> bool('yes')
True
>>> bool('no')
True
>>> bool('')
False
>>> bool('')     #empty string only false#
False
>>> #str()
>>> str(100)
'100'
>>> str(0B1111)
'15'
>>> str(0+1j)
'1j'
>>> str(10.5)
'10.5'
>>> str(10+20j)
'(10+20j)'
>>> str(True)
'True'
>>> str(false)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    str(false)
NameError: name 'false' is not defined
>>> str(False)
'False'
>>> 