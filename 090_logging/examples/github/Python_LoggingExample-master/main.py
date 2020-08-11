"""
Basic python example project to showcase how standard logging works.

In the resources directory, there are two logging files:
    * logging.py - An example of "basic" logging. Sets up logging with standard levels.
    * extended_logging.py - The same as above, with logic to add custom log levels as well.
"""

# User Class Imports.
import resources.logging
import resources.extended_logging


def basic_logger_example():
    # Initialize logging with the standard/basic logger.
    logger = resources.logging.get_logger(__name__)

    # Write log statements.
    logger.debug('This is a "DEBUG" level statement. Made with basic logger.')
    logger.info('This is an "INFO" level statement. Made with basic logger.')
    logger.warning('This is a "WARNING" level statement. Made with basic logger.')
    logger.error('This is an "ERROR" level statement. Made with basic logger.')

def extended_logger_example():
    # Initialize logging with the extended logger.
    logger = resources.extended_logging.get_logger(__name__)

    # Write log statements.
    logger.debug('This is a "DEBUG" level statement. Made with extended logger.')
    logger.info('This is an "INFO" level statement. Made with extended logger.')
    logger.warning('This is a "WARNING" level statement. Made with extended logger.')
    logger.error('This is an "ERROR" level statement. Made with extended logger.')
    logger.testresult('This is a "TESTRESULT" level statement. Made with extended logger.')

if __name__ == '__main__':
    basic_logger_example()
    extended_logger_example()

