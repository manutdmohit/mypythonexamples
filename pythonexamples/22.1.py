Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='abcdefghij'
>>> s[0:-10:-1]
''
>>> s[0:-11:-1]
'a'
>>> s[0:0:1]
''
>>> s[0:-9:-2]
''
>>> s[-5:-9:-2]
'fd'
>>> s[10:-1:-1]
''
>>> s[10000:2:-1]
'jihgfed'
>>> 