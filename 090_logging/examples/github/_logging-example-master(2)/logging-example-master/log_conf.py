# -*- coding: utf-8 -*-

import logging  # docs:  https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
#    logging from multiple python modules:  https://docs.python.org/3/howto/logging.html#logging-from-multiple-modules
#      also, see this :  https://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules
import logging.handlers  # required for using additional handlers
# import logging.config  # if using a config file


def singleton(cls):  # singleton, how to:  https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()


@singleton
class Logger():
    def __init__(self):
        """ Create a logger and attach some handlers with individual formatters.
        """
        # logging.config.fileConfig('logging.conf')  # if using a config file
        # self.logger = logging.getLogger('root')  # if you want to use the (default) 'root' logger

        # Create (a) logger  (this is different from the "root" logger, which I'm not gonna be using)
        self.logger = logging.getLogger('mylog')  # name of the logger
        self.logger.setLevel(logging.DEBUG)  # set a "default" log level; individual handlers re-set this

        # Stream handler (prints to STDOUT)
        stream_handler = logging.StreamHandler()
        formatter_1 = logging.Formatter(
            fmt='%(asctime)s | %(levelname).3s | %(message)s'
        )  # string format operations explanations:    https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
        #       % start of formatter
        #         () mapping key; to LogRecord attributes, see:  https://docs.python.org/3.4/library/logging.html#logrecord-attributes
        #         .(dot) acts as "trim"
        #         -(minus) is "left adjusted"
        #         3 is the number of characters to apply effect
        #       s signifies string (end of formatter)
        #
        #   # color in formatter (TODO):  https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
        #
        stream_handler.setFormatter(formatter_1)
        stream_handler.setLevel(logging.INFO)

        # File handler (writes to a file)
        logFilePath = 'logging-example.log'
        file_handler = logging.handlers.RotatingFileHandler(logFilePath, mode='w')  # 'a' for append
        formatter_2 = logging.Formatter(
            fmt='%(asctime)s | %(name)-20s | %(levelname)-10s | %(message)s'
        )
        file_handler.setFormatter(formatter_2)
        file_handler.setLevel(logging.DEBUG)  # DEBUG (plus all other levels) appear in .log file only.

        # Attach handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)
