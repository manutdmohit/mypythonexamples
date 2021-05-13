supermarket={
               'store1':{
			       'name':'Nepal',
			       'items':[
				              {'name':'soap','quantity':20},
			                  {'name':'brush','quantity':30},
						      {'name':'pen','quantity':40}
						   ]
                 },
			     'store2':{
			        'name':'Nepal1',
			        'items':[
					           {'name':'Python','quantity':200},
			                   {'name':'Java','quantity':300},
						       {'name':'Perl','quantity':400}
				            ]
				  }		    
                  
             }
print('Name of the Store1:')
print(supermarket['store1']['name'])
print('The items in store1 are:')
for d in supermarket['store1']['items']:
	print(d['name'])
print('The number of Python Books in store 2:')
for d in supermarket['store2']['items']:
	if d['name']=='Python':
		print(d['quantity'])