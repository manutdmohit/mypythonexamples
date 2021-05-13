import json
with open('emp.json','r') as f:
	employee=json.load(f)
for k,v in employee.items():
	print(k,':',v)

'''name : durga
age : 35
salary : 1000.0
isMarried : True
isHavingGF : None'''