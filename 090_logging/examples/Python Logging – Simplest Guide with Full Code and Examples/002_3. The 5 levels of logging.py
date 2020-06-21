# logging has 5 different hierarchical levels of logs that a given logger may be configured to.
#
# Lets see what the python docs has to say about each level:
#
# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened,
# or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50
# Now, coming back to the previous question of what would have happened had you not setup logging.basicConfig
# (level=logging.INFO) in the previous example.
#
# The answer is: the log would not have been printed because, the default logger is the root and its
# default basicConfig level is WARNING. That means, only messages from logging.warning() and higher levels will get
# logged.
# So, the message of logging.info() would not be printed. And that is why the basic config was set as INFO initially
# (in logging.basicConfig(level=logging.INFO)).
# Had I set the level as logging.ERROR instead, only message from logging.error and logging.critical will be logged.

import logging
logging.basicConfig(level=logging.WARNING)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}

logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

#> WARNING:root:a=3 and b=3 are equal
#> ERROR:root:a=-1 and b=4 cannot be negative
#> CRITICAL:root:Hypotenuse of a, b is 5.0

