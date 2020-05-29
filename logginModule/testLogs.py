#! /root/anaconda3/bin/python3.7
import inspect
import logging
from basicLogs import testLogs2, testLogs3, threadingExample

import os
from datetime import datetime, date
from basicLogs import logger_settings
k = 0

api_logger = logger_settings.api_logger
# while True:
#     print(k)
#     k = k + 1
class loggBS:
    def testMethod(self):
        print("* " * 40)
        workingDirectory = 'C:/Users/piyush12.kumar/PycharmProjects/logsInPython/basicLogs'
        microserviceName = 'forecastingEngine'
        serverIP = '10.64.216.92'
        timeFormat = '%d-%b-%Y-%I-%M-%S-%p'
        now = datetime.now()
        current_time = now.strftime(timeFormat)
        logfileName = microserviceName + '_' + serverIP + '_' + current_time
        logDirectory = 'logs3'
        directory = workingDirectory + '/' + logDirectory
        if not os.path.isdir(directory):
            os.mkdir(directory)
        else:
            print("os.path.isdir(directory) = ", os.path.isdir(directory))

        # FMT = '%H-%M-%S'
        FMT = '%Y-%m'
        current_time = now.strftime(FMT)
        directory = workingDirectory + '/' + logDirectory + '/' + current_time

        if not os.path.isdir(directory):
            os.mkdir(directory)
        else:
            print("os.path.isdir(directory) = ", os.path.isdir(directory))

        logging.basicConfig(filename=directory + '/' + logfileName,
                            format='[%(asctime)s] : [%(levelname)s]: %(message)s', datefmt='%d-%b-%Y %I:%M:%S %p',
                            level=logging.DEBUG)

    def dologging(self):
        # print(inspect.stack()[0][3])
        # loggerr = logger_settings.get_logger_instance()
        # loggerrr = logging.getLogger("api_logger")
        # x = loggerrr.handlers
        # print(type(x))
        # print(loggerrr.handlers)
        # logName = 'logName'
        # handler = logging.FileHandler(os.path.join('C:/Users/piyush12.kumar/PycharmProjects/logsInPython/basicLogs'
        #                                            '/logs/', logName + '.log'), 'w')
        # loggerrr.addHandler(handler)
        # print(loggerrr.handlers)
        api_logger.debug('This message should go to the log file ' )
        api_logger.info('So should this')
        api_logger.warning('And this, too')
        api_logger.info('Started')
        testLogs2.do_something()
        api_logger.info('Finished')
        testLogs3.testClassForLogs().testLogMethod()
        threadingExample.runThreads()
        api_logger.info('Finished in the end')

    def debugLog(self, message, methodName=None, className=None):
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.debug(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className)

    def infoLog(self, message, methodName=None, className=None):
        # message = 'This message should go to the log file having info log'
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.info(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className)

    def warningLog(self, message, methodName=None, className=None):
        # message = 'This message should go to the log file having warning log'
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.warning(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className)

    def errorLog(self, message, methodName=None, className=None):
        # message = 'This message should go to the log file having error log'
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.error(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className)

    def criticalLog(self, message, methodName=None, className=None):
        # message = 'This message should go to the log file having critical log'
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.critical(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className)

    def exceptionLog(self, message, methodName=None, className=None):
        # message = 'This message should go to the log file having critical log'
        if className is None:
            className = 'NA'
        if methodName is None:
            methodName = 'NA'
        api_logger.exception(message + ' | METHOD NAME :: ' + methodName + ' | CLASS NAME :: ' + className,stack_info=True)


if __name__ == '__main__':

    # while True:
    #     logger_settings.get_logger_instance().debug('This message should go to the log file ')
    #     logger_settings.get_logger_instance().info('So should this')
    #     logger_settings.get_logger_instance().warning('And this, too')
    #     logger_settings.get_logger_instance().info('Started')
    # loggBS().testMethod()
    loggBS().dologging()
