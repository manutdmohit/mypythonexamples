Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f1():
	print('Hello')

	
>>> print(f1)
<function f1 at 0x000001699A7300D0>
>>> print(id(f1))
1553074421968
>>> def wish(name):
	print('Good Morning:',name)

	
>>> greeting=wish
>>> print(id(wish))
1553074838976
>>> p
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> print(id(greeting))
1553074838976
>>> wish('Durga')
Good Morning: Durga
>>> greeting('Durga')
Good Morning: Durga
>>> del wish
>>> greeting('Sunny')
Good Morning: Sunny
>>> def outer():
	print('outer execution started')
	def inner():
		print('inner function execution')

		
>>> def outer():
	print('outer execution started')
	def inner():
		print('inner function execution')
	print('outer funtion execution completed')

	
>>> outer()
outer execution started
outer funtion execution completed
>>> inner()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    inner()
NameError: name 'inner' is not defined
>>> outer().inner()
outer execution started
outer funtion execution completed
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    outer().inner()
AttributeError: 'NoneType' object has no attribute 'inner'
>>> def outer():
	print('outer execution started')
	def inner():
		print('inner function execution')
	inner()	
	print('outer funtion execution completed')

	
>>> outer()
outer execution started
inner function execution
outer funtion execution completed
>>> inner()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    inner()
NameError: name 'inner' is not defined
>>> def outer():
	def inner():
		print('inner function execution')
	return inner

>>> f1=outer()
>>> print(f1)
<function outer.<locals>.inner at 0x000001699A795D30>
>>> f1()
inner function execution
>>> f1()
inner function execution
>>> f1()
inner function execution
>>> f1()
inner function execution
>>> outer()
<function outer.<locals>.inner at 0x000001699A7300D0>
>>> df f1(func):
	
SyntaxError: invalid syntax
>>> def f1(func):
	func()

	
>>> def f2():
	print('f2 funtion')

	
>>> f1(f2)
f2 funtion
>>> list=[1,2,3,4,5,6,7,8,9,10]
>>> def is_even(n):
	if n%2==0:
		return True
	else:
		return False

	
>>> filter(is_even,list)
<filter object at 0x000001699A786EE0>
>>> list2=list(filter(is_even,list))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list2=list(filter(is_even,list))
TypeError: 'list' object is not callable
>>> list1=[1,2,3,4,5,6,7,8,9,10]
>>> def is_even(n):
	if n%2==0:
		return True
	else:
		return False

	
>>> list2=list(filter(is_even,list1))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    list2=list(filter(is_even,list1))
TypeError: 'list' object is not callable
>>> print(list(filter(is_even,list1)))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(list(filter(is_even,list1)))
TypeError: 'list' object is not callable
>>> 
=================== RESTART: D:/Python/Python38/filter()1.py ===================
[2, 4, 6, 8, 10]
>>> 