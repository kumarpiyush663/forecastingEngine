import threading
import time
from basicLogs import testLogs
import inspect


def do_something(message, seconds):
    print(f"sleeping for {1} sec ....")
    time.sleep(1)
    for _ in range(100):
        testLogs.loggBS().debugLog(message, inspect.stack()[0][3])
    print('slept for 1 sec ')


def do_something_info(message, seconds):
    print(f"sleeping for {1} sec ....")
    time.sleep(1)
    for _ in range(100):
        testLogs.loggBS().infoLog(message, inspect.stack()[0][3])
    print('slept for 1 sec ')


def runThreads():

    start_time = time.perf_counter()
    for i in range(10):
        t = threading.Thread(target=do_something, args=[' in debug log thread No ' + str(i), i])
        t.start()

    for i in range(10):
        t = threading.Thread(target=do_something_info, args=['thread No ' + str(i) + ' in info log', i])
        t.start()

    time.sleep(59)
    for i in range(10):
        t = threading.Thread(target=do_something, args=['Again in debug log thread No ' + str(i), i])
        t.start()
    end_time = time.perf_counter()

    for i in range(10):
        t = threading.Thread(target=do_something_info, args=['thread No ' + str(i) + ' in info log again', i])
        t.start()

    print(end_time - start_time)
# do_something()
# do_something()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# end_time = time.perf_counter()
#
# print(end_time - start_time)
