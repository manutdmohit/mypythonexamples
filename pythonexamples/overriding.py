class Parent:
    def property(self):
        print('Land+Gold+Cash+Power')
    def marry(self):
        print('Sita')
class Child(Parent):
    def marry(self):
        print('Durga')
c=Child()
c.property()
c.marry()                    