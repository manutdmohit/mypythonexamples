Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=12.5
>>> type(f)
<class 'float'>
>>> 0B111
7
>>> 0o123
83
>>> 0x123
291
>>> type(0b111)
<class 'int'>
>>> type(0o123)
<class 'int'>
>>> f=1.234
>>> f=0B1.1011
SyntaxError: invalid syntax
>>> f=1.2e3      #exponentiAL form/scientic notification
>>> prinf(f)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    prinf(f)
NameError: name 'prinf' is not defined
>>> f=1.2e3
>>> print(f)
1200.0
>>> f=1.2e3
>>> f
1200.0
>>> f=1.2e3      #exponentiAL form/scientic notification#
>>> f
1200.0
>>> f=1.2e3      #exponentiAL form/scientic notification#
>>> print(f)
1200.0
>>> #complex data type#
>>> x=10+20j
>>> type(x)
<class 'complex'>
>>> x=10+20J
>>> x
(10+20j)
>>> x=10+20i
SyntaxError: invalid syntax
>>> print(x.real)
10.0
>>> print(x.imag)
20.0
>>> x=10.5+20j
>>> x=10.5+20.6j
>>> x=0b1111+20j
>>> x=15+0B1111j
SyntaxError: invalid syntax
>>> x
(15+20j)
>>> x=10+20j
>>> y=20+30j
>>> x+y
(30+50j)
>>> x*y
(-400+700j)
>>> x/y
(0.6153846153846154+0.0769230769230769j)
>>> hepl
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    hepl
NameError: name 'hepl' is not defined
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(rand)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    help(rand)
NameError: name 'rand' is not defined
>>> rand
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    rand
NameError: name 'rand' is not defined
>>> x
(10+20j)
>>> help(random)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    help(random)
NameError: name 'random' is not defined
>>> rand()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    rand()
NameError: name 'rand' is not defined
>>> #Boolean#
>>> b=true
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b=true
NameError: name 'true' is not defined
>>> b=True
>>> type(b)
<class 'bool'>
>>> a=10
>>> b=20
>>> c=a>b
>>> print(c)
False
>>> type(c)
<class 'bool'>
>>> print(True+True)
2
>>> prine(True-False)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    prine(True-False)
NameError: name 'prine' is not defined
>>> print(True-False)
1
>>> #True=1# #False=0#
>>> #String str#
>>> s='Ram'
>>> print(type(s)0
      
SyntaxError: invalid syntax
>>> print(type(s)
      121
      
SyntaxError: invalid syntax
>>> s='durga'
>>> print(type(s))
<class 'str'>
>>> s='a'
>>> print(type(a))
<class 'int'>
>>> print(type(s))
<class 'str'>
>>> print(s)
a
>>> s
'a'
>>> s='raaaa
SyntaxError: EOL while scanning string literal
>>> s=raaaa
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s=raaaa
NameError: name 'raaaa' is not defined
>>> s='durga
SyntaxError: EOL while scanning string literal
>>> 
=============== RESTART: D:/Python/Python38/10.1.py ===============
>>> s='raaa
SyntaxError: EOL while scanning string literal
>>> exit()
>>> clear()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> z='rrrr
SyntaxError: EOL while scanning string literal
>>>  s="raaaaaaa
 
SyntaxError: unexpected indent
>>> s='''raaaaa
         sdsdsdsd''''
SyntaxError: EOL while scanning string literal
>>> s='''rsdsdsadasda
dsdsad'''
>>> print(s)
rsdsdsadasda
dsdsad
>>> s="""sdsdsdsdsd
hbdhsadhashd"""
>>> print(s)
sdsdsdsdsd
hbdhsadhashd
>>> s='ram is a goo boy'
>>> print(s)
ram is a goo boy
>>> s='ram is a good boy'
>>> print(s)
ram is a good boy
        
