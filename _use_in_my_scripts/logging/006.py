# Do not get logger at the module level unless disable_existing_loggers is False
# You can see lots of examples out there are getting the loggers at the module level, including this article.
# I did it just for making the example simple. While this looks harmless, but in fact, there is a pitfall. The problem is, Python logging module by default respects all existing logger before you load the configuration from a file if you get logger at the module level like this
#
# my_module.py:

import logging

logger = logging.getLogger(__name__)

def foo():
    logger.info('Hi, foo')

class Bar(object):
    def bar(self):
        logger.info('Hi, bar')
# main.py
#
import logging

# load my module
import my_module

# load the logging configuration
logging.config.fileConfig('logging.ini')

# my_module.foo()
# bar = my_module.Bar()
# bar.bar()
# logging.ini
#
# [loggers]
# keys=root
#
# [handlers]
# keys=consoleHandler
#
# [formatters]
# keys=simpleFormatter
#
# [logger_root]
# level=DEBUG
# handlers=consoleHandler
#
# [handler_consoleHandler]
# class=StreamHandler
# level=DEBUG
# formatter=simpleFormatter
# args=(sys.stdout,)
#
# [formatter_simpleFormatter]
# format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
# datefmt=
# And you expect to see the records appear in the log, but you will see nothing. Why? Because you create the logger at
# the module level, you then import the module before loading the logging configuration from a file.
# The logging.fileConfig and logging.dictConfig function's default behavior is to disable existing loggers when they are
# called. So, those setting in the file will not be applied to your logger in my_module.py. Its better to get
# the logger when you need it to avoid the pitfall. Its cheap to create or get a logger. You can write the code like this:
#
import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')


# By doing that, the loggers will be created after you load the configuration. Now the setting will be applied correctly.
# Other than avoiding create logger at the module level, since Python 2.7, a new argument disable_existing_loggers was
# added to the logging.fileConfig function, and disable_existing_loggers key is also added in the schema
# forlogging.dictConfig function. By setting it to False, the problem mentioned above can be solved. For example:

import logging
import logging.config

logger = logging.getLogger(__name__)

# load config from file
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
# or, for dictConfig
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
})

logger.info('It works!')