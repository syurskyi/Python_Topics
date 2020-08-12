__author__ = 'Luke Skibinski <l.skibinski@elifesciences.org>'
__copyright__ = 'eLife Sciences'
__license__ = 'GPLv3'

import logging

logger = logging.getLogger(__name__)

def foo():
    logger.info("beginning foo")
    raise SystemExit("THE COMPUTER SAYS 'NO'")
