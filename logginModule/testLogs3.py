from basicLogs import testLogs
import inspect
from basicLogs.logger_settings import api_logger


class testClassForLogs():
    def testLogMethod(self):
        message = 'This message should go to the log file having debug log'
        className = self.__class__.__name__
        # print(logger_settings.get_logger_instance().getLogger(__name__))

        testLogs.loggBS().debugLog(message, inspect.stack()[0][3], className)
