from zipfile import *
f=ZipFile('filedemo.zip','r',ZIP_STORED)
names=f.namelist()
print(names)
for name in names:
    f1=open(name,'r')
    text=f1.read()
    print('File Name:',name)
    print('Content of this file:')
    print(text)
    print()
    f1.close()