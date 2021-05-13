Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[10,20,[30,40]]
>>> print(l[0])
10
>>> print(l[1])
20
>>> print(l[2])
[30, 40]
>>> print(l[2][0])
30
>>> l=[]
>>> for i in range(1,11):
	l.append(i)

	
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(1,11):
	l.append(i*i)

	
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> l=[]
>>> for i in range(1,11):
	l.append(i*i)

	
>>> print(l)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> l=[2*x for x in range(1,11)]
>>> print(l)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> l=[2*x for x in range(1,6)]
>>> print(l)
[2, 4, 6, 8, 10]
>>> l=[2**x for x in range(1,6)]
>>> print(l)
[2, 4, 8, 16, 32]
>>> l=[x for x in range(1,101)if x%10==-]
SyntaxError: invalid syntax
>>> l=[x for x in range(1,101)if x%10==0]
>>> print(l)
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> l=[x for x in range(1,101)if x%10==6]
>>> print(l)
[6, 16, 26, 36, 46, 56, 66, 76, 86, 96]
>>> l1=[10,20,30,40]
>>> l2=[30,40,50,60]
>>> l3=[x for x in l1 if x not in l2]
>>> print(l3)
[10, 20]
>>> l3=[x for x in l1 if x in l2]
>>> print(l3)
[30, 40]
>>> l=['Ram','Sita','Hari','Gopi']
>>> l1=[word[0] for word in l]]