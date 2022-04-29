import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
from threading import Lock
lock = Lock()
with lock:
    print('Lock is held')


# Example 2
lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()


# Example 3
import logging
logging.getLogger().setLevel(logging.WARNING)
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


# Example 4
my_function()


# Example 5
from contextlib import contextmanager
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


# Example 6
with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()


# Example 7
with open('my_output.txt', 'w') as handle:
    handle.write('This is some data!')


# Example 8
@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


# Example 9
with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')


# Example 10
logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
