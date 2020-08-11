'Example Logging Module'
import logging

# Create a module level logger using the module name as imported
# Add this to all of your modules to enable logging.
logger = logging.getLogger(__name__)

def log_message(message):
    'Log a message'

    logger.debug('Asked to log message: %s', message)
    logger.info('Logging Message in Module: %s', message)
