# Working With the Stack
# There are a similar set of functions for performing the same operations with the current call stack instead of
# a traceback.
#
# print_stack()

import traceback
import sys

from traceback_example import call_function

def f():
    traceback.print_stack(file=sys.stdout)

print 'Calling f() directly:'
f()

print
print 'Calling f() from 3 levels deep:'
call_function(f)

# $ python traceback_print_stack.py
#
# Calling f() directly:
#   File "traceback_print_stack.py", line 19, in <module>
#     f()
#   File "traceback_print_stack.py", line 16, in f
#     traceback.print_stack(file=sys.stdout)
#
# Calling f() from 3 levels deep:
#   File "traceback_print_stack.py", line 23, in <module>
#     call_function(f)
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 22, in call_function
#     return call_function(f, recursion_level-1)
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 22, in call_function
#     return call_function(f, recursion_level-1)
#   File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 24, in call_function
#     return f()
#   File "traceback_print_stack.py", line 16, in f
#     traceback.print_stack(file=sys.stdout)