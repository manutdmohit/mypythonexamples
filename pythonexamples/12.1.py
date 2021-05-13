Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #frozenset
>>> #immutable
>>> s={10,20,30,40}
>>> s.add(50)
>>> s.remove(50)
>>> print(s)
{40, 10, 20, 30}
>>> s={10,20,30,40}
>>> fs-frozenset(s)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fs-frozenset(s)
NameError: name 'fs' is not defined
>>> fs=frozenset(s)
>>> print(fs)
frozenset({40, 10, 20, 30})
>>> print(type(fs))
<class 'frozenset'>
>>> fr.add(50)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fr.add(50)
NameError: name 'fr' is not defined
>>> fr.remove(50)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fr.remove(50)
NameError: name 'fr' is not defined
>>> fs.add(50)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fs.add(50)
AttributeError: 'frozenset' object has no attribute 'add'
>>> fs.remove(30)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fs.remove(30)
AttributeError: 'frozenset' object has no attribute 'remove'
>>> s={10,20,30,40,40,50}
>>> print(fs)
frozenset({40, 10, 20, 30})
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> #dict