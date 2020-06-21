# And print_exception() uses format_exception():

import traceback
import sys
from pprint import pprint

from traceback_example import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'format_exception():'
    exc_type, exc_value, exc_tb = sys.exc_info()
    pprint(traceback.format_exception(exc_type, exc_value, exc_tb))

# $ python traceback_format_exception.py
#
# format_exception():
# ['Traceback (most recent call last):\n',
#  '  File "traceback_format_exception.py", line 17, in <module>\n    produce_exception()\n',
#  '  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception\n    produce_exception(recursion_level-1)\n',
#  '  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception\n    produce_exception(recursion_level-1)\n',
#  '  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 18, in produce_exception\n    raise RuntimeError()\n',
#  'RuntimeError\n']

