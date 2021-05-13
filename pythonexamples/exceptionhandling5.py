try:
    print(10/0)
except ArithmeticError:
    print('Arithmetic Error')        
except ZeroDivisionError:
    print('Zero Division Error')    
