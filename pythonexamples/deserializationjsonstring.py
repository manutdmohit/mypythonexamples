import json
json_string='''{
    "name": "durga",
    "age": 35,
    "salary": 1000.0,
    "isMarried": true,
    "isHavingGF": null
}'''
employee=json.loads(json_string) #topythondict
#print(type(employee))
print('Employee Name:',employee['name'])
print('Employee Age:',employee['age'])
print('Employee Salary:',employee['salary'])
print('Is Employee Married:',employee['isMarried'])
print('Does Employee has GF:',employee['isHavingGF'])

for k,v in employee.items():
	print(k,":",v)

'''Employee Name: durga
Employee Age: 35
Employee Salary: 1000.0
Is Employee Married: True
Does Employee has GF: None
name : durga
age : 35
salary : 1000.0
isMarried : True
isHavingGF : None'''