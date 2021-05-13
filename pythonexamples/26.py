Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d['A']=100
>>> d['B']=200
>>> print(d)
{'A': 100, 'B': 200}
>>> d['A']=300
>>> print(d)
{'A': 300, 'B': 200}
>>> d.get('A')
300
>>> d.get('Z')
>>> print(d.get('Z'))
None
>>> d.get('A',0)
300
>>> d.get('Z',0)
0
>>> d['A']=1
>>> d['B']=2
>>> d['A']=d.get('A',0)+1
>>> print(d)
{'A': 2, 'B': 2}
>>> 