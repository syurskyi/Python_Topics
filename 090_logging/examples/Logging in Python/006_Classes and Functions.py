# Classes and Functions
# So far, we have seen the default logger named root, which is used by the logging module whenever its functions
# are called directly like this: logging.debug(). You can (and should) define your own logger by creating an object of
# the Logger class, especially if your application has multiple modules. Lets have a look at some of the classes and
# functions in the module.
# The most commonly used classes defined in the logging module are the following:
#
# Logger: This is the class whose objects will be used in the application code directly to call the functions.
#
# LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event being
# logged, like the name of the logger, the function, the line number, the message, and more.
#
# Handler: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is
# a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send
# the logging outputs to corresponding destinations, like sys.stdout or a disk file.
#
# Formatter: This is where you specify the format of the output by specifying a string format that lists out
# the attributes that the output should contain.
#
# Out of these, we mostly deal with the objects of the Logger class, which are instantiated using the module-level
# function logging.getLogger(name). Multiple calls to getLogger() with the same name will return a reference
# to the same Logger object, which saves us from passing the logger objects to every part where its needed.
# Here is an example:

import logging

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
# This is a warning

# This creates a custom logger named example_logger, but unlike the root logger, the name of a custom logger is not
# part of the default output format and has to be added to the configuration. Configuring it to a format to show
# the name of the logger would give an output like this:
#
# WARNING:example_logger:This is a warning
# Again, unlike the root logger, a custom logger cant be configured using basicConfig(). You have to configure it
# using Handlers and Formatters: