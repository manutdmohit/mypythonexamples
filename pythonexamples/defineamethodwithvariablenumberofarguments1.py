class Test:
    def m1(self,*args):
        print('variable length argument method')
t=Test()
t.m1()
t.m1(10)
t.m1(10,20,30)
t.m1(10,20,30,40,50,60)        