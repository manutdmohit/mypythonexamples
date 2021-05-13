import logging

logger=logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

fileHandler=logging.FileHandler(filename='abc.log',mode='w')

formatter1=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
formatter2=logging.Formatter('%(levelname)s:%(message)s')

consoleHandler.setFormatter(formatter2)
fileHandler.setFormatter(formatter1)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')
