cart=[10,20,600,40,50]
for item in cart :
	if item>500:
		print("we can't place this order because of insurance issue ")
		break
	print('Processing item:',item)
else:
	print('All items processed successfully')