class Human:
    def __init__(self,name):
        print('Human Object Creation...')
        self.name=name
        self.head=self.Head()
    
    def info(self):
        print('Hello, myself',self.name)
        print('I am fully busy with')
        self.head.talk()
        self.head.brain.think()    
    class Head:
        def __init__(self):
            print('Head Object Creation...')
            self.brain=self.Brain()
        
        def talk(self):
            print('Talking...')
        class Brain:
            def __init__(self):
                print('Brain Object Creation')
            
            def think(self):
                print('Thinking...')    

human=Human('Durga')
human.info()                        
