# The FileHandler() and Formatter() classes are used to setup the output file and the format of messages for loggers
# other than the root logger.Do you remember how we setup the filename and the format of the message in the root logger
# (inside logging.basicConfig()) earlier? We just specified the filename and format parameters in logging.basicConfig()
# and all subsequent logs went to that file.However, when you create a separate logger, you need to set them up
# individually using the logging.FileHandler() and logging.Formatter() objects. A FileHandler is used to make your
# custom logger to log in to a different file. Likewise, a Formatter is used to change the format of your logged
# messages.
#
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')

# Notice how we set the formatter on the file_handler and not the logger directly.
# Assuming the above code is run from the main program, if you look inside the working directory,
# a file named logfile.log will be created if it doesnt exist and would contain the below messages.
#
# #> 2019-02-17 12:40:14,797 : WARNING : __main__ : Something is not right.
# #> 2019-02-17 12:40:14,798 : ERROR : __main__ : A Major error has happened.
# #> 2019-02-17 12:40:14,798 : CRITICAL : __main__ : Fatal error. Cannot continue

# Note again, the Formatter is set on the FileHandler object and not directly on the logger. Something you may want to
# get used to.