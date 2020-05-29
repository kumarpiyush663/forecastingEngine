from logging.config import dictConfig
import logging
import os
from datetime import datetime, date

logInstance = {}


# def loggingInfo(logLevel, logDirectory, logFileName):
workingDirectory = 'C:/Users/piyush12.kumar/PycharmProjects/logsInPython/basicLogs'
microserviceName = 'forecastingEngine'
serverIP = '10.64.216.92'
timeFormat = '%d-%b-%Y-%I-%M-%S-%p'
now = datetime.now()
current_time = now.strftime(timeFormat)
logFileName = microserviceName + '_' + serverIP + '_' + current_time
logDirectory = 'logs4'
logLevel = logging.DEBUG
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

# logging.basicConfig(filename=directory + '/' + logfileName,
#                     format='[%(asctime)s] : [%(levelname)s]: %(message)s', datefmt='%d-%b-%Y %I:%M:%S %p',
#                     level=logging.DEBUG)

logging_config = dict(

    version=1,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s] : [%(levelname)s] "
                       "[%(funcName)s:%(lineno)s] %(message)s"),
            'datefmt': '%d-%b-%Y %I:%M:%S %p',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'api-logger': {'class': 'logging.handlers.RotatingFileHandler',
                       'formatter': 'verbose',
                       'level': logLevel,
                       'filename': directory + '/' + logFileName,
                       'maxBytes': 8192000,
                       'backupCount': 50},
        'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
                                 'formatter': 'verbose',
                                 'level': logLevel,
                                 'filename': directory + '/' + logFileName,
                                 'maxBytes': 8192000,
                                 'backupCount': 50}
        # ,'console': {
        #     'class': 'logging.StreamHandler',
        #     'level': 'DEBUG',
        #     'formatter': 'simple',
        #     'stream': sys.stdout,
        # },
    },
    loggers={
        'api_logger': {
            'handlers': ['api-logger'],
            'level': logging.DEBUG
        },
        'batch_process_logger': {
            'handlers': ['batch-process-logger'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)

api_logger = logging.getLogger('api_logger')
batch_process_logger = logging.getLogger('batch_process_logger')




# def get_logger_instance():
#     workingDirectory = 'C:/Users/piyush12.kumar/PycharmProjects/logsInPython/basicLogs'
#     microserviceName = 'forecastingEngine'
#     serverIP = '10.64.216.92'
#     timeFormat = '%d-%b-%Y-%I-%M-%S-%p'
#     now = datetime.now()
#     current_time = now.strftime(timeFormat)
#     logfileName = microserviceName + '_' + serverIP + '_' + current_time
#     logFolder = 'logs4'
#     logLevel = logging.DEBUG
#     logDirectory = workingDirectory + '/' + logFolder
#     if not os.path.isdir(logDirectory):
#         os.mkdir(logDirectory)
#     # else:
#     #     print("os.path.isdir("+logDirectory+") = ", os.path.isdir(logDirectory))
#
#     # FMT = '%H-%M-%S'
#     FMT = '%Y-%m-%d-%H-%M'
#     current_time = now.strftime(FMT)
#     directory = workingDirectory + '/' + logFolder + '/' + current_time
#
#     if not os.path.isdir(directory):
#         os.mkdir(directory)
#         # logInstance.clear()
#     # else:
#     #     print("os.path.isdir("+directory+") = ", os.path.isdir(directory))
#         # return logInstance.get(directory)
#
#     logInstanceVar = loggingInfo(logLevel, directory, logfileName)
#     logInstance[directory] = logInstanceVar
#     return logInstanceVar
