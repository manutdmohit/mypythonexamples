import pickle
f=open('emp.ser','rb')
print('Deserialize Emp object and printing data')
while True:
	try:
		e=pickle.load(f)
		e.display()
	except EOFError:
		break
print('All Employees Created')
