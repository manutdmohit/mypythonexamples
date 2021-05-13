class Test:
    def m1(self):
        def calc(a,b):
            print('The Sum:',a+b)
            print('The Product:',a*b)
            print('The Difference:',a-b)
            print('The Average:',(a+b)/2)
        calc(10,20)
        calc(100,200)
        calc(1000,2000)    

t=Test()
t.m1()

