# format_stack() prepares the stack trace in the same way that format_exception() prepares the traceback.
#
# traceback_format_stack.py

import traceback
import sys
from pprint import pprint

from traceback_example import call_function


def f():
    return traceback.format_stack()


formatted_stack = call_function(f)
pprint(formatted_stack)

# It returns a list of strings, each of which makes up one line of the output.
#
# $ python3 traceback_format_stack.py
#
# ['  File "traceback_format_stack.py", line 21, in <module>\n'
#  '    formatted_stack = call_function(f)\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 24, in call_function\n'
#  '    return call_function(f, recursion_level - 1)\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 24, in call_function\n'
#  '    return call_function(f, recursion_level - 1)\n',
#  '  File '
#  '".../traceback_example.py", '
#  'line 26, in call_function\n'
#  '    return f()\n',
#  '  File "traceback_format_stack.py", line 18, in f\n'
#  '    return traceback.format_stack()\n']

