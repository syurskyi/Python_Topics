# -*- coding: utf-8 -*-

import logging
import os
import sys


FORMATTER = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s\t%(message)s')
#: The log directory. Will be created if it doesn't exist yet.
LOG_DIR = "Logs_" + __package__.capitalize()
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logger = logging.getLogger(__package__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(FORMATTER)
logger.addHandler(ch)


def add_file_handler(logger, level, tag):
    """
    Adds a ``logging.FileHandler`` handler to the specified ``logging`` instance that will log
    the messages it receives at the specified error level or greater.  The log file will be named
    as outlined in ``get_logfile_name``.

    Args:
        logger: The `logging.Logger` instance to add the `logging.FileHandler` to.
        level:  `int`. A logging level (i.e. given by one of the constants `logging.DEBUG`,
            `logging.INFO`, `logging.WARNING`, `logging.ERROR`, `logging.CRITICAL`).
        tag: `str`. A tag name to add to at the end of the log file name for clarity on the
            log file's purpose.
    """
    filename = get_logfile_name(tag)
    handler = logging.FileHandler(filename=filename, mode="a")
    handler.setLevel(level)
    handler.setFormatter(FORMATTER)
    logger.addHandler(handler)

def get_logfile_name(tag):
    """
    Creates a log file name that will be prefixed with the path of `LOG_DIR`.
    The file path will be '$LOG_DIR/log_$TAG.txt', where
    $TAG is the value of the 'tag' parameter.

    Args:
        tag: `str`. A tag name to add to at the end of the log file name for clarity on the
            log file's purpose.
    """
    filename = "log_" + tag + ".txt"
    filename = os.path.join(LOG_DIR, filename)
    return filename
