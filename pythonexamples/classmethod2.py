class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flyting with {} wings'.format(name,cls.wings))
Bird.fly('Parrot')
Bird.fly('Eagle')       
