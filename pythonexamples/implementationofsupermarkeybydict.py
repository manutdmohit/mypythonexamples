supermarket={
'store1':{
      'name':'Durga General Store',
	  'items':[
	       {'name':'soap','quantity':20},
		   {'name':'brush','quantity':30},
		   {'name':'pen','quantity':40},
		  ]
    },
'store2':{
      'name':'Sunny Book Store',
	  'items':[
	       {'name':'python','quantity':100},
		   {'name':'django','quantity':200},
		   {'name':'java','quantity':300},
		  ]
    }
}
print('Name of the store1:')
print(supermarket['store1']['name'])
#print(supermarket.get('store1').get('name'))
print('The Names of all items present in store1:')
for d in supermarket['store1']['items']:
	print(d['name'])
print('The number of django books in store2:')
for d in supermarket['store2']['items']:
	if d['name']=='django':
		print(d['quantity'])





 