import json
employee={'name':'durga','age':35,'salary':1000.0,'isMarried':True,'isHavingGF':None}
json_string=json.dumps(employee,indent=4,sort_keys=True) #tostring
print(json_string) 
'''{
        "name": "durga",
        "age": 35,
        "salary": 1000.0,
        "isMarried": true,
        "isHavingGF": null
}'''
'''{
    "age": 35,
    "isHavingGF": null,
    "isMarried": true,
    "name": "durga",
    "salary": 1000.0
}'''
with open('emp.json','w') as f:
	json.dump(employee,f,indent=4) #tofile
print('open emp.json to see jsondata') 
