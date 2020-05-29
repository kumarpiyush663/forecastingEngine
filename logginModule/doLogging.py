import inspect

from basicLogs.logger_settings import api_logger
from basicLogs import testLogs,testLogs2,testLogs3,threadingExample
class loggBS:


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

    def checkErrorLog(self):
        try:
            x = 5/0
        except Exception as e:
            print(e)
            print(type(e))
            testLogs.loggBS().exceptionLog("Input your Custom error message", "method Name","className")