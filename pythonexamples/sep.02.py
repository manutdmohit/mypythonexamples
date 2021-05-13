Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1={100:'A',200:'B'}
>>> d1={300:'c',400:'d'}
>>> d1={100:'A',200:'B'}
>>> d2={300:'C',400:'D'}
>>> d1+d2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d1+d2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d3=d1+d2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d3=d1+d2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d4=d1*3
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d4=d1*3
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> d1==d2
False
>>> d1!=d2
True
>>> d3={200:'B',100:'A'}
>>> d1==d3
True
>>> d1<d2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d1<d2
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> print(100 in d1)
True
>>> print(300 in d1)
False
>>> print('A' in d1)
False
>>> d1={100:'A',200:'B',300:'C'}
>>> d={100:'A',200:'B',300:'C'}
>>> len(d)
3
>>> d.get(100)
'A'
>>> d.get(700)
>>> 