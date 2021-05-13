import logging
logging.basicConfig(filename='29sep.txt',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info('A new request came')
try:
    x=int(input('Enter First Number'))
    y=int(input('Enter Second Number'))
    print('The Result:',x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('Please provide int values only')
    logging.exception(msg)

logging.info('A request processing completed')    