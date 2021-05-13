class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input('Enter Age:'))
if age>60:
    raise TooYoungException('Please wait some more time,definitely you will get last match')   
elif age<18:
    raise TooOldException('Your age already crossed marriage age,no chance of getting married')
else:
    print('Thanks for registration, you will get match details soon by email')
