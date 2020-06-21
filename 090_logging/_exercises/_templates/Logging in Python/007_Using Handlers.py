# Handlers come into the picture when you want to configure your own loggers and send the logs to multiple places when they are generated. Handlers send the log messages to configured destinations like the standard output stream or a file or over HTTP or to your email via SMTP.
#
# A logger that you create can have more than one handler, which means you can set it up to be saved to a log file and
# also send it over email.
#
# Like loggers, you can also set the severity level in handlers. This is useful if you want to set multiple handlers
# for the same logger but want different severity levels for each of them. For example, you may want logs with level
# WARNING and above to be logged to the console, but everything with level ERROR and above should also be saved to
# a file. Here is a program that does that:
#
# # logging_example.py

______ l____

# Create a custom logger
logger = l____.getLogger(__name__)

# Create handlers
c_handler = l____.StreamHandler()
f_handler = l____.FileHandler('file.log')
c_handler.setLevel(l____.WARNING)
f_handler.setLevel(l____.ERROR)

# Create formatters and add it to handlers
c_format = l____.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = l____.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
# __main__ - WARNING - This is a warning
# __main__ - ERROR - This is an error

# Here, logger.warning() is creating a LogRecord that holds all the information of the event and passing it to all
# the Handlers that it has: c_handler and f_handler.
# c_handler is a StreamHandler with level WARNING and takes the info from the LogRecord to generate an output in
# the format specified and prints it to the console. f_handler is a FileHandler with level ERROR, and it ignores
# this LogRecord as its level is WARNING.
#
# When logger.error() is called, c_handler behaves exactly as before, and f_handler gets a LogRecord at the level
# of ERROR, so it proceeds to generate an output just like c_handler, but instead of printing it to console,
# it writes it to the specified file in this format:
#
# 2018-08-03 16:12:21,723 - __main__ - ERROR - This is an error
# The name of the logger corresponding to the __name__ variable is logged as __main__, which is the name Python assigns
# to the module where execution starts. If this file is imported by some other module, then the __name__ variable would
# correspond to its name logging_example. Here is how it would look:
#
# # run.py
#
# ______ logging_example
# logging_example - WARNING - This is a warning
# logging_example - ERROR - This is an error