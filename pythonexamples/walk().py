import os
g=os.walk('material')
for dirpath,dirnames,filenames in g:
	print('directory path:',dirpath)
	print('directory name:',dirnames)
	print('file name:',filenames)
	print()