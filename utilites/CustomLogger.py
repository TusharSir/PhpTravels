import inspect
import logging

#
# class LogGenerator:
#     @staticmethod
#     def loggen():
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
#         logging.basicConfig(filename="D:\\Credence Python Projects by Tushar Sir\\PhpTravels\\Logs\\automationLogfile.log",
#                             format='%(asctime)s :%(levelname)s : %(name)s :%(message)s')
#         #logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("D:\\Credence Python Projects by Tushar Sir\\PhpTravels\\Logs\\automationLogfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger