import logging
logging.basicConfig(format='%(levelname)s:%(name)s:%(process)s:%(message)s:%(module)s:%(lineno)d')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')
