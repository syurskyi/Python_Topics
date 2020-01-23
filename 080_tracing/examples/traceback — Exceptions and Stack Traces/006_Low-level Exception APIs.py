# print_exc() is just a shortcut for print_exception(), which requires explicit arguments.

# traceback_print_exception.py
import traceback
import sys

from traceback_example import produce_exception

try:
    produce_exception()
except Exception as err:
    print('print_exception():')
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb)

# The arguments to print_exception() are produced by sys.exc_info().
#
# $ python3 traceback_print_exception.py
#
# Traceback (most recent call last):
#   File "traceback_print_exception.py", line 16, in <module>
#     produce_exception()
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 19, in produce_exception
#     raise RuntimeError()
# RuntimeError
# print_exception():

