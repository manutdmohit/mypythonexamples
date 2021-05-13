class Customer:
    '''This class Developed by Durga and describes bank operations'''
    bankname='DURGABANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount 
        print('After deposit,balance:',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient Funds...cannot perform this operation')
        else:
            self.balance=self.balance-amount
            print('After withdraw,balance:',self.balance)           

print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input('choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter Amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount to withdraw:')) 
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks for Banking')
        break
    else:
        print('your option is invalid....please choose valid option')      
