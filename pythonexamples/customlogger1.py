import logging
logger=logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler(filename='custtest.log',mode='w')
fileHandler.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')
