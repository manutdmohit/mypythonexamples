class SportsNews:
    def sportsInfo(self):
        print('Sports-Information 1')
        print('Sports-Information 2')
        print('Sports-Information 3')
        print('Sports-Information 4')
class MovieNews:    
    def moviesInfo(self):
        print('Movies-Information 1')
        print('Movies-Information 2')
        print('Movies-Information 3')
        print('Movies-Information 4')
class PoliticsNews:
        def politicsInfo(self):
            print('Politics-Information 1')
            print('Politics-Information 2')
            print('Politcis-Information 3')
            print('Politics-Information 4')        

class DurgaNews:
    def __init__(self):
        self.sports=SportsNews()
        self.movies=MovieNews()
        self.politics=PoliticsNews()
    def getTotalNews(self):
        print('Welcome to Durga News:')
        self.sports.sportsInfo()
        self.movies.moviesInfo()
        self.politics.politicsInfo()

dnews=DurgaNews()
dnews.getTotalNews()


