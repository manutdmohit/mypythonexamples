from emp import *
import pickle
f=open('emp.ser','wb')
while True:
	eno=int(input('Enter ENO:'))
	ename=input('Enter ENAME:')
	esal=float(input('Enter ESAL:'))
	eaddr=input('Enter EADDR:')
	e=Employee(eno,ename,esal,eaddr)
	pickle.dump(e,f)
	option=input('Do you want to serialize another object[yes/No]:')
	if option.lower()=='no':
		break
print('Multiple Employee objects serialized')
