"""
Logging initialization with option to add custom log levels.
In this example, we create a new logging level of "TESTRESULT" that logs higher than critical.

Note: Standard log priority is "NOTSET" > "DEBUG" > "INFO" > "WARNING" > "ERROR" > "CRITICAL".

Default log level numerical values:
    CRITICAL 	50
    ERROR 	    40
    WARNING 	30
    INFO 	    20
    DEBUG 	    10
    NOTSET 	    0
"""

# System Imports.
import logging.config, os


def get_logger(caller):
    """
    Returns an instance of the logger. Always pass the __name__ attribute.
    By calling through here, guarantees that logger will always have proper settings loaded.
    :param caller: __name__ attribute of caller.
    :return: Instance of logger, associated with caller's __name__.
    """
    return logging.getLogger(caller)


def addLoggingLevel(levelName, levelNum, methodName=None):
    """
    Code directly imported from https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.
    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.
    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present
    Example
    -------
    >> addLoggingLevel('TRACE', logging.DEBUG - 5)
    >> logging.getLogger(__name__).setLevel("TRACE")
    >> logging.getLogger(__name__).trace('that worked')
    >> logging.trace('so did this')
    >> logging.TRACE
    5
    """
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
       raise AttributeError('{} already defined in logging module'.format(levelName))
    if hasattr(logging, methodName):
       raise AttributeError('{} already defined in logging module'.format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
       raise AttributeError('{} already defined in logger class'.format(methodName))

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)
    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)

addLoggingLevel('TESTRESULT', 55)


# Find project_dir logging path.
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(project_dir, 'resources/logs')
if not os.path.exists(log_dir):
    print('Creating logging folders.')
    os.makedirs(log_dir)


# Dictionary style logging options.
LOGGING = {
    'version': 1,
    'formatters': {
        # Minimal logging. Only includes message.
        'minimal': {
            'format': '%(message)s',
        },
        # Simple logging. Includes message type and actual message.
        'simple': {
            'format': '[%(levelname)s] [%(filename)s %(lineno)d]: %(message)s',
        },
        # Basic logging. Includes date, message type, file originated, and actual message.
        'standard': {
            'format': '%(asctime)s [%(levelname)s] [%(filename)s %(lineno)d]: %(message)s',
        },
        # Verbose logging. Includes standard plus the process number and thread id.
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] [%(filename)s %(lineno)d] || %(process)d %(thread)d || %(message)s',
        },
    },
    'handlers': {
        # Sends log message to the void. May be useful for debugging.
        'null': {
            'class': 'logging.NullHandler',
        },
        # To console.
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        # Debug Level - To file.
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'debug.log'),
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'formatter': 'standard',
        },
        # Info Level - To file.
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'info.log'),
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'formatter': 'standard',
        },
        # Warn Level - To file.
        'file_warn': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'warn.log'),
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        # Error Level - To file.
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'error.log'),
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        # TestResult Level - To file.
        'file_test_result': {
            'level': 'TESTRESULT',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, 'test_result.log'),
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'formatter': 'minimal',
},
    },
    'loggers': {
        # All basic logging.
        '': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_warn', 'file_error', 'file_test_result'],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}


# Load dictionary of settings into logger.
logging.config.dictConfig(LOGGING)

# Test logging.
logger = get_logger(__name__)
logger.info('Logging initialized.')
logger.debug('Logging directory: {0}'.format(log_dir))


# Test a "test_result" level log message.
# logger.testresult('This is a "TESTRESULT level log message.')
