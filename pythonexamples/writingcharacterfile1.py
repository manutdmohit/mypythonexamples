f=open('abc1.txt','w')
l=['Sunny\n','Bunny\n','Chinny\n','Bunny\n']
f.writelines(l)
print('List of lines written to the file successfully')
f.close()