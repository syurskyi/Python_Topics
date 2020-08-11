# -*- coding: utf-8 -*-

import logging

def do_stuff():
    # While harmless in Python3, avoid initializing the module logger
    # at import, because this can confuse you if you import it before
    # loading the configuration in main.
    log = logging.getLogger(__name__)  # Getting loggers is "cheap".
    log.info('Logging from another module.')
