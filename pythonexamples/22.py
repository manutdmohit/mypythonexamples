Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='abcdefghijk'
>>> s[2:7]
'cdefg'
>>> s[:7]
'abcdefg'
>>> s[2:]
'cdefghijk'
>>> s[:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[:]
'abcdefghijk'
>>> s[2:6:1]
'cdef'
>>> s[2:7:1]
'cdefg'
>>> s[2:7:2]
'ceg'
>>> s[2:7:3]
'cf'
>>> s[::2]
'acegik'
>>> s[2:7:4]
'cg'
>>> s[::3]
'adgj'
>>> 