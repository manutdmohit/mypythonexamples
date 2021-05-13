class Outer:
    def __init__(self):
        print('Outer class object creation')
    
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation')
            def m1(self):
                print('Nested Inner class method')    
o=Outer()
i=o.Inner()
ii=i.InnerInner()
ii.m1()


