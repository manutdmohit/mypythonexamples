import pickle
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))

e=Employee(100,'Durga',10000,'Hyd')
with open('emp.str','wb') as f:
	pickle.dump(e,f)
print('Pickling of Employee Object completed')

with open('emp.str','rb') as f:
	newobj=pickle.load(f)
print('Unpickling of Employee ojbect completed')
print('Printing Employee Information...')
newobj.display()