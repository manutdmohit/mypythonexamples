import logging
import logging.config
logging.config.fileConfig("logging_config.init")
logger=logging.getLogger('demologger')
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('it is info message')
logger.debug('It is debug message')