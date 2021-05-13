Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #special operators
>>> # Identity operators
>>> # membership operaots
>>> # membership operators
>>> # Identity operators
>>> # is     is not
>>> a=20
>>> b=20
>>> print(a is b)
True
>>> print(a is not b)
False
>>> b=30
>>> print(a is b)
False
>>> print(a is not b)
True
>>> a='ram'
>>> b='sita'
>>> print(a is b)
False
>>> b='ram'
>>> print(a is b)
True
>>> print(a is not b)
False
>>> l1=[10,20,30,40]
>>> l2=[10,20,30,40]
>>> print(id(l1))
2121285807424
>>> print(id(l2))
2121285829696
>>> print(l1 is l2)
False
>>> print(l1 is not l2)
True
>>> print(l1 == l2)
True
>>> # membership operators
>>> 0 in [1,2,4,4]
False
>>> 0 not in [1,2,4,4]
True
>>> s=' hello i am learning python'
>>> print('h' in s)
True
>>> print('d' in s)
False
>>> print('d' not in s)
True
>>> print('python' in s)
True
>>> print('Python' in s)
False
>>> l=['sunny', 'bunny', 'chinny' , 'vinny']
>>> print('sunny' in l)
True
>>> print('pinny' in l)
False
>>> l[0]
'sunny'
>>> print('pinny' not in l)
True
>>> #operator precedence
>>> print(10+2*3)
16
>>> print((10+2)*3)
36
>>> a=10
>>> b=20
>>> a=30
>>> c=10
>>> d=5
>>> a=30
>>> print((a+b)*c/d)
100.0
>>> print((a+b)*(c/d))
100.0
>>> print((a+(b*c)/d))
70.0
>>> 3/2*4+3+(10/5)**3-2
15.0
>>> 1.5*4
6.0
>>> #mathematical funtions from math module
>>> #code resuability
>>> import math
>>> print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> gcd(4,8)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    gcd(4,8)
NameError: name 'gcd' is not defined
>>> c=gcd(4,8)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c=gcd(4,8)
NameError: name 'gcd' is not defined
>>> sqrt 16
SyntaxError: invalid syntax
>>> sqrt(16)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sqrt(16)
NameError: name 'sqrt' is not defined
>>> print(sqrt(16))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(sqrt(16))
NameError: name 'sqrt' is not defined
>>> import math
>>> print(math.gcd(8,4))
4
>>> print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']









>>> 


>>> 




>>> 


>>> 



>>> 


>>> 



>>> 



>>> 

>>> 