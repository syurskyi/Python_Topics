# You can configure logging as shown above using the module and class functions or by creating a config file or
# a dictionary and loading it using fileConfig() or dictConfig() respectively. These are useful in case you want
# to change your logging configuration in a running application.
#
# Here is an example file configuration:

# In the above file, there are two loggers, one handler, and one formatter. After their names are defined,
# they are configured by adding the words logger, handler, and formatter before their names separated by an underscore.
#
# To load this config file, you have to use fileConfig():

import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
# 2018-07-13 13:57:45,467 - __main__ - DEBUG - This is a debug message
# The path of the config file is passed as a parameter to the fileConfig() method, and the disable_existing_loggers
# parameter is used to keep or disable the loggers that are present when the function is called. It defaults to True if
# not mentioned.
