# print_exception() uses format_exception() to prepare the text.

# traceback_format_exception.py
import traceback
import sys
from pprint import pprint

from traceback_example import produce_exception

try:
    produce_exception()
except Exception as err:
    print('format_exception():')
    exc_type, exc_value, exc_tb = sys.exc_info()
    pprint(
        traceback.format_exception(exc_type, exc_value, exc_tb),
        width=65,
    )

# The same three arguments, exception type, exception value, and traceback, are used with format_exception().
#
# $ python3 traceback_format_exception.py
#
# format_exception():
# ['Traceback (most recent call last):\n',
#  '  File "traceback_format_exception.py", line 17, in
# <module>\n'
#  '    produce_exception()\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 17, in produce_exception\n'
#  '    produce_exception(recursion_level - 1)\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 17, in produce_exception\n'
#  '    produce_exception(recursion_level - 1)\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 19, in produce_exception\n'
#  '    raise RuntimeError()\n',
#  'RuntimeError\n']