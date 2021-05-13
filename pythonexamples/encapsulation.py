class Account:
    def __init__(self,initial_balance):
        self.__balance=initial_balance
    def getBalance(self):
        return self.__balance    
    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print(self.__balance)
    def withdraw(self,amount):
        self.__balance=self.__balance-amount  
        print(self.__balance)
a=Account(10000)
a.deposit(5000)
a.withdraw(2500)         
    

