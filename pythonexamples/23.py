Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'durga'+'soft'
'durgasoft'
>>> 'durga'+10
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'durga'+10
TypeError: can only concatenate str (not "int") to str
>>> 'durga'+10.0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    'durga'+10.0
TypeError: can only concatenate str (not "float") to str
>>> 'durga'+True
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'durga'+True
TypeError: can only concatenate str (not "bool") to str
>>> 'durga'+'True'
'durgaTrue'
>>> 'durga'*3
'durgadurgadurga'
>>> 3*'durga'
'durgadurgadurga'
>>> 'd' in durga
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'd' in durga
NameError: name 'durga' is not defined
>>> 'd' in 'durga'
True
>>> 'z' in 'durga'
False
>>> 'z' not in 'durga'
True
>>> 'durga' < 'ravi'
True
>>> ord('d)
    
SyntaxError: EOL while scanning string literal
>>> ord('d')
100
>>> ord('r')
114
>>> 'ramba' <'ramya'
True
>>> 'ramba' >'ramba'
False
>>> 'ramba' >='ramba'
True
>>> s='ABCBAa'
>>> s='ABCBA'
>>> print(s.find('B'))
1
>>> print(s.find('Z'))
-1
>>> print(s.rfind('B'))
3
>>> print(s.rfind('Z'))
-1
>>> s='ABCDEGHJJBK'
>>> print(s.find('B',3,8))
-1
>>> s='ABCDEGHJBK'print(s.find('B',3,8))
SyntaxError: invalid syntax
>>> s='ABCDEGHJBK'
>>> print(s.find('B',3,8))
-1
>>> print(s.rfind('B',3,8))
-1
>>> print(s.rfind('F',3,8))
-1
>>> s='ABCDEFGHJBK'
>>> print(s.rfind('F',3,8))
5
>>> find('F',3,7)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    find('F',3,7)
NameError: name 'find' is not defined
>>> s='ABCBA'
>>> print(s.index('B'))
1
>>> print(s.index('Z'))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(s.index('Z'))
ValueError: substring not found
>>> print(s.rindex('B'))
3
>>> print(s.rindex('Z'))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(s.rindex('Z'))
ValueError: substring not found
>>> s='ABCDEFGHIJKLMN'
>>> primt(s.index('B'))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    primt(s.index('B'))
NameError: name 'primt' is not defined
>>> print(s.index('B'))
1
>>> print(s.index('B',4,8))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(s.index('B',4,8))
ValueError: substring not found
>>> print(s.index('F',4,8))
5
>>> print(s.index('DEF',4,8))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(s.index('DEF',4,8))
ValueError: substring not found
>>> print(s.index('F',4,8))
5
>>> s='ABCDE'
>>> print(s.index('D',2,100))
3
>>> print(s.index('F',2,100))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(s.index('F',2,100))
ValueError: substring not found
>>> print(s.index('F',4,1000))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(s.index('F',4,1000))
ValueError: substring not found
>>> print(s.index('F',4,100))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(s.index('F',4,100))
ValueError: substring not found
>>> s='ABCDEFGHIJKLMN'
>>> print(s.index('F',4,100))
5
>>> print(s.index('FFF',4,1000))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(s.index('FFF',4,1000))
ValueError: substring not found
>>> 