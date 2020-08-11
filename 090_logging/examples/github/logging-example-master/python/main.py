#!/usr/bin/env python
__author__ = 'Luke Skibinski <l.skibinski@elifesciences.org>'
__copyright__ = 'eLife Sciences'
__license__ = 'GPLv3'

import logging
import config
import someothermodule

logger = logging.getLogger(__name__)

logger.debug("program started")
logger.info("Security is one of your major goals in life.")
logger.warn("Some of your aspirations tend to be pretty unrealistic.")

try:
    logger.debug("attempting to do something tricksy")
    someothermodule.foo()
except:
    logger.exception("caught unhandled exception.")
finally:
    logger.info("program exiting, cleaning up")
