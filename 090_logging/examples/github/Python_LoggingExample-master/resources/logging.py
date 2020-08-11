"""
Logging initialization.

Note: Standard log priority is "NOTSET" > "DEBUG" > "INFO" > "WARNING" > "ERROR" > "CRITICAL".
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
    },
    'loggers': {
        # All basic logging.
        '': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_warn', 'file_error'],
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
