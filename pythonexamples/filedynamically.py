fname=input('Enter File Name:')
f=open(fname,'w')
while True:
    data=input('Enter data to write:')
    f.write(data+'\n')
    option=input('Do you want to add some more data[yes/no]')
    if option.lower()=='no':
        break
f.close()
print('Data written to the file successfully')    