from zipfile import *
f=ZipFile('filedemo.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
print('filedemo.zip created successfully')