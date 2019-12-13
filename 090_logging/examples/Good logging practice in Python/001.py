# Use Python standard logging module
# So, how do you do logging correctly? Its easy, use the standard Python logging module.
# Thanks to the Python community, logging is a standard module, it was well designed to be easy-to-use and
# very flexible. You can use the logging system like this:

import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')


# INFO:__main__:Start reading database
# INFO:__main__:Updating records ...
# INFO:__main__:Finish updating records


# You can run it and see
# What is different between the print approach you asked. Well, of course, there are benefits:
# You can control message level and filter out not important ones
# You can decide where and how to output later
# There are different importance levels you can use, DEBUG, INFO, WARNING, ERROR, and CRITICAL. By giving different
# level to the logger and handler, you can write only error messages to a specific log file, or record debug details
# when debugging. Lets change the logger level to DEBUG and see the output again
#
# logging.basicConfig(level=logging.DEBUG)

# As you can see, the debugging records now appear in the output. Like we mentioned previously,
# besides changing the log level, you can also decide how to process these messages