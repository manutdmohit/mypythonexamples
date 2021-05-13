Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[10,20]
>>> l2=[30,40]
>>> l3=l1+l2
>>> print(l3)
[10, 20, 30, 40]
>>> l1=[(10,20,30),(40,50,60)]
>>> print(l1[0][1])
20
>>> print(l1[1][2])
60
>>> d={'cars':('Innova','Honda','Maruti'),'mobiles':('Samsung','Iphone','Nokia')}
>>> print(d['cars'][1])
Honda
>>> print(d['cars'])
('Innova', 'Honda', 'Maruti')
>>> print(d.get(cars))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(d.get(cars))
NameError: name 'cars' is not defined
>>> print(d.get('cars'))
('Innova', 'Honda', 'Maruti')
>>> print(d.get('cars')[1])
Honda
>>> fox x in d['mobiles']:
	
SyntaxError: invalid syntax
>>> for x in d['mobiles']:
	print(x)

	
Samsung
Iphone
Nokia
>>> print(d['mobiles'])
('Samsung', 'Iphone', 'Nokia')
>>> s={(10,20,30)}
>>> print(s)
{(10, 20, 30)}
>>> s={[10,20,30]}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s={[10,20,30]}
TypeError: unhashable type: 'list'
>>> s={(10,20,30),[40,50,60]}
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s={(10,20,30),[40,50,60]}
TypeError: unhashable type: 'list'
>>> s={(10,20,30):'item1'}
>>> print(s)
{(10, 20, 30): 'item1'}
>>> s={(10,20,30):'item1',[40,50,60]:'item2'}
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s={(10,20,30):'item1',[40,50,60]:'item2'}
TypeError: unhashable type: 'list'
>>> s={(10,20,30):'item1',(40,50,60):[70,80,90]}
>>> print(s)
{(10, 20, 30): 'item1', (40, 50, 60): [70, 80, 90]}
>>> 