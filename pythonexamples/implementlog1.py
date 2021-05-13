import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='w')
print('Logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')
