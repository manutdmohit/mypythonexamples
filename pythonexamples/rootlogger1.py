import logging
logging.basicConfig(filename='root.log',level=logging.DEBUG)
import student
logging.critical('It is critical message')
logging.error('It is error message')
logging.warning('It is warning message')
logging.info('It is Info message')
logging.debug('It is debug message')