# print_exc() is just a shortcut for print_exception(), which requires explicit arguments:

import traceback
import sys

from traceback_example import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'print_exception():'
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb)


# $ python traceback_print_exception.py
#
# Traceback (most recent call last):
#   File "traceback_print_exception.py", line 16, in <module>
#     produce_exception()
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception
#     produce_exception(recursion_level-1)
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception
#     produce_exception(recursion_level-1)
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 18, in produce_exception
#     raise RuntimeError()
# RuntimeError
# print_exception():

