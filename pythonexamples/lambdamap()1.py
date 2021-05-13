l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)
l4=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(l4)