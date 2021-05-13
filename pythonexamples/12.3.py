Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #None Data Type
>>> #no value associated
>>> def f1():
	 return(10)
	x=f1()
	
SyntaxError: unindent does not match any outer indentation level
>>> print(xdef f1():
	 return(10)
      
	x=f1()
      
SyntaxError: invalid syntax
>>> def f1():
	 return(10)
	x=f1()
	
SyntaxError: unindent does not match any outer indentation level
>>> def f1():
	 return(10)
	x=f1()
	
SyntaxError: unindent does not match any outer indentation level
>>> def f1():
	 return(10)
	
	x=f1()
	
SyntaxError: unindent does not match any outer indentation level
>>> def f1():
	 return(10)
     x=f1()
     
SyntaxError: unindent does not match any outer indentation level
>>> def f1()
SyntaxError: invalid syntax
>>> def f1():
	return 10
x=f1()
SyntaxError: invalid syntax
>>> def f1():
	return 10
      x=f1()
      
SyntaxError: unindent does not match any outer indentation level
>>> def f1():
	return 10
  x=f1()
  
SyntaxError: unindent does not match any outer indentation level
>>> a=None
>>> print(id(a))
140726847707264
>>> print(type(a))
<class 'NoneType'>
>>> a=None
>>> b=None
>>> c=None
>>> def f1():
	pass
d=f1()
SyntaxError: invalid syntax
>>> #Escape Characters
>>> # \n : new line
>>> \t : horizontal tab
SyntaxError: unexpected character after line continuation character
>>> #\t : horizontal tab
>>> # \r : carriage return
>>> #\b : back space
>>> #\f : form feed
>>> #\' single quote
>>> # \" double quote
>>> # \\ back slash
>>> print('ram')
ram
>>> print('ram\tsita')
ram	sita
>>> print('ram\nsita')
ram
sita
>>> print('ram\bsita')
ramsita
>>> print('This is\' symbol')
This is' symbol
>>> print('This is \' symbol')
This is ' symbol
>>> print('This is \" symbol')
This is " symbol
>>> print('This is \\ symbol')
This is \ symbol
>>> #comment
>>> # This is single line comment
>>> #constants in python
>>> 