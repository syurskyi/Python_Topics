# There are a similar set of functions for performing the same operations with the current call stack instead of
# a traceback. print_stack() prints the current stack, without generating an exception.

#traceback_print_stack.py

import traceback
import sys

from traceback_example import call_function


def f():
    traceback.print_stack(file=sys.stdout)


print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
call_function(f)

# The output look like a traceback without an error message.
#
# $ python3 traceback_print_stack.py
#
# Calling f() directly:
#   File "traceback_print_stack.py", line 21, in <module>
#     f()
#   File "traceback_print_stack.py", line 17, in f
#     traceback.print_stack(file=sys.stdout)
#
# Calling f() from 3 levels deep:
#   File "traceback_print_stack.py", line 25, in <module>
#     call_function(f)
#   File ".../traceback_example.py", line 24, in call_function
#     return call_function(f, recursion_level - 1)
#   File ".../traceback_example.py", line 24, in call_function
#     return call_function(f, recursion_level - 1)
#   File ".../traceback_example.py", line 26, in call_function
#     return f()
#   File "traceback_print_stack.py", line 17, in f
#     traceback.print_stack(file=sys.stdout)