f=open('abc1.txt','r')
l=f.readlines()
for line in l:
    print(line,end='' )
f.close()    