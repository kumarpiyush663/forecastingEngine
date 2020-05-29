from basicLogs.logger_settings import api_logger


def do_something():
    # print(logger_settings.get_logger_instance().getLogger(__name__))
    api_logger.info('Doing something')
