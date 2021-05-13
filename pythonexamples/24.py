Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='ABABABA'
>>> s=s.replace('A','B')
>>> s='ABABABA'
>>> print(id(s))
2150320808304
>>> s=s.replace('A','B')
>>> print(id(s))
2150310923824
>>> print(s)
BBBBBBB
>>> l=[10,20,30]
>>> print(type(l))
<class 'list'>
>>> l[0]
10
>>> print(type(l[0]))
<class 'int'>
>>> l=[10,20,30]
>>> d='-'.join(l)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d='-'.join(l)
TypeError: sequence item 0: expected str instance, int found
>>> l=['10','20','30']
>>> d='-'.join(l)
>>> print(d)
10-20-30
>>> print('abc123'.isalpha())
False
>>> print('abc123'.isdigit())
False
>>> print('abc123'.isalnum())
True
>>> 
>>> s=mohitsaud
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s=mohitsaud
NameError: name 'mohitsaud' is not defined
>>> s='mohitsaud'
>>> s.append('@gmail.com')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.append('@gmail.com')
AttributeError: 'str' object has no attribute 'append'
>>> s.append(@gmail.com)
SyntaxError: invalid syntax
>>> s.append(1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.append(1)
AttributeError: 'str' object has no attribute 'append'
>>> s.append('1')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.append('1')
AttributeError: 'str' object has no attribute 'append'
>>> s=[12,13,15,16]
>>> s.append('1')
>>> print(s)
[12, 13, 15, 16, '1']
>>> s.append(1)
>>> print(s)
[12, 13, 15, 16, '1', 1]
>>> s=[12,13,15,16]
>>> s.append(1)
>>> print(s)
[12, 13, 15, 16, 1]
>>> email='saudmohit'+'@'+'gmail.com'
>>> print(email)
saudmohit@gmail.com
>>> 