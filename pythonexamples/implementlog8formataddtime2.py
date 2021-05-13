import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')