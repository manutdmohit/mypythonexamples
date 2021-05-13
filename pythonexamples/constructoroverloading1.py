class Test:
    def __init__(self,*args):
        print('Constructor with variable number of arguments')
t=Test()
t=Test(10)
t=Test(10,20,40,50,60)        