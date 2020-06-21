# To examine the current stack, construct a StackSummary from walk_stack().

#
# traceback_stacksummary.py
import traceback
import sys

from traceback_example import call_function


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    print(''.join(summary.format()))


print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
call_function(f)

# The format() method produces a sequence of formatted strings ready to be printed.
#
# $ python3 traceback_stacksummary.py
#
# Calling f() directly:
#   File "traceback_stacksummary.py", line 18, in f
#     traceback.walk_stack(None)
#   File "traceback_stacksummary.py", line 24, in <module>
#     f()
#
#
# Calling f() from 3 levels deep:
#   File "traceback_stacksummary.py", line 18, in f
#     traceback.walk_stack(None)
#   File ".../traceback_example.py", line 26, in call_function
#     return f()
#   File ".../traceback_example.py", line 24, in call_function
#     return call_function(f, recursion_level - 1)
#   File ".../traceback_example.py", line 24, in call_function
#     return call_function(f, recursion_level - 1)
#   File "traceback_stacksummary.py", line 28, in <module>
#     call_function(f)