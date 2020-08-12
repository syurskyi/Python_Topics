#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from log_conf import Logger  # logger initialisation takes place during the
#     first import of the log_conf module, while instantiating the
#     (singleton) Logger class.


Logger.logger.info('Hello World')

def main():
    logger = Logger.logger  # for simplicity

    # Usage example:
    logger.info('Started')
    try:
        logger.warning('potential problem...')
        x = 1337
        y = 0
        z = x / y
    except Exception as ex:
        logger.error('Operation failed.')
        # .debug log level messages will only show up in .log file
        logger.debug('Encountered "{0}" when trying to perform calculation.'.format(ex))
    logger.info('Ended')


if __name__ == '__main__':
    main()
    import mymodule  # access the same logger instance from a different module
    Logger.logger.info('Bye!')
