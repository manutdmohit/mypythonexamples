n=int(input('Enter no. of students:'))
d={}
for i in range(n):
	name=input('Enter name of student:')
	marks=int(input('Enter Marks:'))
	d[name]=marks
print('\n')
print('Name','\t\t','Marks')
print('\n')
for name in d:
	print(name,'\t\t',d[name])
