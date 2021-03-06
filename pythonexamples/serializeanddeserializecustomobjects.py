import json
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=Employee(100,'Durga',1000.0,'Hyd')
#e_dict={'eno':e.eno,'ename':e.ename,'esal':e.esal,'eaddr':e.eaddr}
e_dict=e.__dict__
#print(e_dict)
#{'eno': 100, 'ename': 'Durga', 'esal': 1000.0, 'eaddr': 'Hyd'}
#serialization to JSON String
json_string=json.dumps(e_dict,indent=4)
print(json_string)
'''{
    "eno": 100,
    "ename": "Durga",
    "esal": 1000.0,
    "eaddr": "Hyd"
}'''
#serialization to JSON File
with open('emp.json','w') as f:
	json.dump(e_dict,f,indent=4)
#Derialization to Python
with open('emp.json','r') as f:
	edict=json.load(f)
e=Employee(edict['eno'],edict['ename'],edict['esal'],edict['eaddr'])
e.display()

