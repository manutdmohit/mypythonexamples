import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t2
t4=t3
del t3,t4
print(sys.getrefcount(t1))