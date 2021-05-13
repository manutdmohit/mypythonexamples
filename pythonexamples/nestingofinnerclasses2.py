class Human:
    class Head:
        def talk(self):
            print('talking...' )
        class Brain:
            def think(self):
                print('thinking...')
human=Human()
head=human.Head()
head.talk()
brain=head.Brain()
brain.think()                    