# extract_stack()

import traceback
import sys
from pprint import pprint

from traceback_example import call_function

def f():
    return traceback.extract_stack()

stack = call_function(f)
pprint(stack)

# $ python traceback_extract_stack.py
#
# [('traceback_extract_stack.py', 19, '<module>', 'stack = call_function(f)'),
#  ('/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py',
#   22,
#   'call_function',
#   'return call_function(f, recursion_level-1)'),
#  ('/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py',
#   22,
#   'call_function',
#   'return call_function(f, recursion_level-1)'),
#  ('/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py',
#   24,
#   'call_function',
#   'return f()'),
#  ('traceback_extract_stack.py', 17, 'f', 'return traceback.extract_stack()')]
