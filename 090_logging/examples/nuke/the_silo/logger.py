import sys
import logging


def create_logger():
    logger = logging.getLogger('The Silo')
    logger.handlers = []

    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = logging.Formatter(fmt='%(name)s: %(asctime)s: '
                                      '%(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


logger = create_logger()
