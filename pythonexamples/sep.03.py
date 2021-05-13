Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={100:'A',200:'B',300:'C',400:'D'}
>>> print(d.pop(300))
C
>>> print(d)
{100: 'A', 200: 'B', 400: 'D'}
>>> print(d.pop(700))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(d.pop(700))
KeyError: 700
>>> print(d.pop(700,'E'))
E
>>> 
>>> print(d)
{100: 'A', 200: 'B', 400: 'D'}
>>> d={100: 'A', 200: 'B', 300: 'C'}
>>> print(d.popitem())
(300, 'C')
>>> print(d)
{100: 'A', 200: 'B'}
>>> print(d.popitem())
(200, 'B')
>>> print(d)
{100: 'A'}
>>> print(d.popitem())
(100, 'A')
>>> print(d.popitem())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(d.popitem())
KeyError: 'popitem(): dictionary is empty'
>>> print(d)
{}
>>> d={100:'A',200:'B',300:'C',400:'D'}
>>> d.clear()
>>> print(d)
{}
>>> 