import os
fname=input('Enter File Name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    f=open(fname,'r')
    text=f.read()
    print('The content of the file is:')
    print('*'*40)
    print(text)
    print('*'*40)
    f.close
else:
    print('File does not exist:',fname)    