str='free 12345 Code Camp'
str=str
data=[]
innerList=[]
for y in range(20):
    innerList.append(y)
for x in str:
    if x.isdigit():
        if x in innerList:
            data.append(x)

print(data)