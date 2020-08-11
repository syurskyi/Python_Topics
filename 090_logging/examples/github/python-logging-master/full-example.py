#!/usr/bin/env python3
import logging
import argparse
import configparser
import requests
import sample_module

CONFIG_FILE = 'logsample.ini'

# Logger for this module, not the root logger
logger = logging.getLogger('full-example')

# Initialize Config file and get the default log_level
config = configparser.ConfigParser()
config.read(CONFIG_FILE)
log_level = int(config['main']['log_level'])

# Parse Command Line Arguments
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Logging Example Program')
parser.add_argument("-level", help="Set logging level", type=str, \
                    choices=['debug', 'info', 'warning', 'critical'])
parser.add_argument("-tracebacks", help="Enable Tracebacks on Errors in Logs", \
                    action="store_true")
parser.add_argument("-warn_urllib3", help="Set urllib3 to log at WARNING", \
                    action="store_true")
parser.add_argument("-v", help="Verbose Output", action="store_true")
args = parser.parse_args()

# Verbose option enables INFO level logging
if args.v:
    log_level = logging.INFO

# -level option maps to different logging levels
if args.level:
    if args.level == 'debug':
        log_level = logging.DEBUG
    elif args.level == 'info':
        log_level = logging.INFO
    elif args.level == 'warning':
        log_level = logging.WARNING
    elif args.level == 'critical':
        log_level = logging.CRITICAL

def init_logging():
    'Initialize Logging Globally'

    # Specify our log format for handlers
    log_format = logging.Formatter('%(asctime)s %(name)s:%(levelname)s: %(message)s')

    # Get the root_logger to attach log handlers to
    root_logger = logging.getLogger()

    # Set root logger to debug level always
    # Control log levels at log handler level
    root_logger.setLevel(logging.DEBUG)

    # Console Handler (always use log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(log_format)
    root_logger.addHandler(ch)


    # Logfile Handler
    fh = logging.FileHandler(config['main']['log_file'])

    # Always log at INFO or below
    if log_level < logging.INFO:
        fh.setLevel(log_level)
    else:
        fh.setLevel(logging.INFO)
    
    # Attach logfile handler
    fh.setFormatter(log_format)
    root_logger.addHandler(fh)

# Initialize Log Handlers
init_logging()

if args.warn_urllib3:
    # Set urllib3 logging to WARNING
    logging.getLogger('urllib3').setLevel(logging.WARNING)

# Logging Message Examples
logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')
logger.critical('Critical Message')

# Test Module level logging
sample_module.log_message('Testing')

# Test requests logging
url = 'https://www.google.com'
logger.debug('Requesting URL: %s', url)
r = requests.get(url)

if r.status_code == 200:
    logger.info('Successfully retrieved URL: %s', url)
logger.debug('First 50 chars returned from URL: %s', r.text[:50])


logger.debug('Testing Divide by 0 exception')
try:
    1/0
except Exception as e:
    if args.tracebacks:
        logger.error(e, exc_info=True)
    else:
        logger.error(e)
    #logger.exception('Divide by 0')
