class Test:
    def sum(self,*args):
        total=0
        for x in args:
            total=total+x
        print('The Sum:',total)

t=Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30) 
t.sum(10,20,30,40,50,60) 

