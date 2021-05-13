from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda x,y:x*y,l)
print(result) 