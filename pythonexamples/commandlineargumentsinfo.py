from sys import argv
print('The number of command line arguments:',len(argv))
print('The list of cmd line arguments:',argv)
print('The cmd line arguments one by one:')
for x in argv:
	print(x)
