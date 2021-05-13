Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=int(input('Enter two integers:'))
Enter two integers:12
>>> a,b=int(input('Enter two integers:'))
Enter two integers:12 232
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a,b=int(input('Enter two integers:'))
ValueError: invalid literal for int() with base 10: '12 232'
>>> 
>>> a,b=int(input('Enter two integers:'))
Enter two integers:12
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a,b=int(input('Enter two integers:'))
TypeError: cannot unpack non-iterable int object
>>> 
>>> a,b=for x in input('Enter two integers:')
SyntaxError: invalid syntax
>>> a,b=for x in input('Enter two integers:')
SyntaxError: invalid syntax
>>> a,b= for x in input('Enter two integers:')
SyntaxError: invalid syntax
>>> a,b= for x in int(input('Enter two integers:'))
SyntaxError: invalid syntax
>>> a,b= (for x in int(input('Enter two integers:')))
SyntaxError: invalid syntax
>>> eval(23)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    eval(23)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> from sys import argu
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    from sys import argu
ImportError: cannot import name 'argu' from 'sys' (unknown location)
>>> from sys import argv
>>> print(type(argv))
<class 'list'>
>>> from sys import argv
>>> print(argv[0])

>>> print(argv[1])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(argv[1])
IndexError: list index out of range
>>> #print()
>>> print(90,100)
90 100
>>> 
>>> print(90,100)
90 100
>>> if 10<20:
	print('10 is less than 20')
    print('end of program')
    
SyntaxError: unindent does not match any outer indentation level
>>> if 10<20:
	print('10 is less than 20')
     print('end of program')
     
SyntaxError: unindent does not match any outer indentation level
>>> 