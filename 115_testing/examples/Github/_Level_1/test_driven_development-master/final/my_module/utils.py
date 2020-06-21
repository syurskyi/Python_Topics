"""

"""

import collections
from time import sleep

def MyFunction(iterable):
    """ Take any object and return if it is iterable or not.
    :param iterable:
    :rtype: bool
    """
    return isinstance(iterable, collections.Iterable)

def MyLongFunction(msg, seconds):
    """ This is an example function that is computationally heavy.

    :param msg: a message to print
    :type msg: str
    :param seconds: n seconds to wait
    :type seconds: int
    :rtype: str
    """

    # To mimic the `heavy computation`
    sleep(seconds)

    return msg.upper()
