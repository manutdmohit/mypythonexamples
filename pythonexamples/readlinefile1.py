f=open('abc1.txt','r')
line=f.readline()
while line!='':
    print(line,end='')
    line=f.readline()
f.close()    