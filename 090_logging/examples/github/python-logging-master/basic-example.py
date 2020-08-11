#!/usr/bin/env python3
import logging
import requests
import sample_module

# Setup basic logging, provide a format for output and set the level to debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
                    level=logging.DEBUG)

# Test logging at different levels
logging.debug('Debug Message')
logging.info('Info Message')
logging.warning('Warning Message')

# Test Module Logging
sample_module.log_message('Module Logging Test')

# Silence sample_module debug messages
logging.getLogger('sample_module').setLevel(logging.INFO)
sample_module.log_message('Module Logging Test without debug')

logging.info('Testing divide by 0 exception')
try:
    1/0
except Exception as e:
    logging.error(e)

    ## Uncomment for stack trace logging
    #logging.error(e, exc_info=True)
