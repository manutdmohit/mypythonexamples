f=None
try:
    f=open('abc.txt','r')
except:
    print('some problem while locationg/opening file')
else:
    print('file opened successfully')
    print('The data present present in the file is:')
    print('#'*50)
    print(f.read())
finally:
    if f is not None:
        f.close()        