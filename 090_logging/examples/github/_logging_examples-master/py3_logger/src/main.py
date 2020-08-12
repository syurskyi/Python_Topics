#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python3 compatible logging setup module to be used as point-of-entry to a
program."""

import argparse
import json
import logging
import logging.config
import os

import example_package.example_module
# We imported example_module before setting logging configuration.
# This can cause issues, see the module for explanation.


def run():
    load_logging_conf('logging.json')
    # All loggers MUST be started AFTER this point, including for imported modules!
    # Start the logger for this module.
    log = logging.getLogger(__name__)

    cli_args = parse_cli_args()

    set_debug_verbosity(cli_args.verbose)

    log.debug('test debug message')
    log.info('test info message')
    log.warn('test warn message')
    log.error('test error message')
    log.critical('test critical message')

    example_package.example_module.do_stuff()


def load_logging_conf(log_cfg_filename):
    """Load logging configuration at '<src_dir>/../logs/<filename>' (os agnostic)."""
    src_dir = os.path.dirname(os.path.realpath(__file__))
    cfg_file_path = os.sep.join((src_dir, '..', 'logs', log_cfg_filename))

    # This will disable all previously existing loggers.
    with open(cfg_file_path) as config_json:
        logging_config = json.load(config_json)
    logging.config.dictConfig(logging_config)


def parse_cli_args():
    """Parse command line args.  Additional options can be added."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', dest='verbose',
                      action='count', default=0,
                      help='increase debug logging level')

    return parser.parse_args()


def set_debug_verbosity(verbosity_counter):
    """Deactivates the debug handler if verbosity_counter is 0, else sets
    the logging level appropriately."""
    debug_handler = logging.root.handlers[1]

    if verbosity_counter == 0:
        logging.root.removeHandler(debug_handler)
    elif verbosity_counter == 1:
        debug_handler.level = logging.INFO
    elif verbosity_counter == 2:
        debug_handler.level = logging.DEBUG
    else:
        debug_handler.level = logging.NOTSET


if __name__ == '__main__':
    run()
