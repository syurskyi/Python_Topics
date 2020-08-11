__author__ = 'Luke Skibinski <l.skibinski@elifesciences.org>'
__copyright__ = 'eLife Sciences'
__license__ = 'GPLv3'

import logging

# 1420811950.9472651 - INFO - elife-api - incoming - foo is in bar, making foobar
# 1420811950.9472651 - INFO - lagotto - metrics - baz bar foo foo bar
FORMAT = logging.Formatter("%(created)f - %(levelname)s - %(processName)s - %(name)s - %(message)s")
DEV_FORMAT = logging.Formatter("%(created)f - %(levelname)s - %(funcName)s:%(lineno)d - %(name)s - %(message)s")

LOGFILE = "./example.log"
DEV_LOGFILE = "example.dev.log"

# http://docs.python.org/2/howto/logging-cookbook.html
logger = logging.getLogger("") # important! this is the *root logger* 
                               # all other loggers are derived from this one
logger.setLevel(logging.DEBUG) # *default* output level

# StreamHandler sends to stderr by default
h = logging.StreamHandler()
h.setLevel(logging.INFO) # output level for *this handler*
h.setFormatter(FORMAT)

# FileHandler sends to a named file
h2 = logging.FileHandler(LOGFILE)
h2.setLevel(logging.WARN) # change to INFO if code is less-than-stable
h2.setFormatter(FORMAT)

# outputs *everything* to a seperate file, good for debugging during dev
h3 = logging.FileHandler(DEV_LOGFILE)
# h3.setLevel(logging.DEBUG) # not neccessary as the root logger outputs at DEBUG
h3.setFormatter(DEV_FORMAT) # for dev you might want a friendlier logging format

logger.addHandler(h)
logger.addHandler(h2)
logger.addHandler(h3)

logger.debug("configuration loaded")
