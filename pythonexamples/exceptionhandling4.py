try:
    print(10/0)
except ZeroDivisionError:
    print('Zero Division Error')
except ArithmeticError:
    print('Arithmetic Error')        