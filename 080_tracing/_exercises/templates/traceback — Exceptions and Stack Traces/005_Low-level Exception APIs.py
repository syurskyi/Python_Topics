# Another way to handle exception reporting is with print_exc(). It uses sys.exc_info() to obtain the exception
# information for the current thread, formats the results, and prints the text to a file handle
# (sys.stderr, by default).

# traceback_print_exc.py
import traceback
import sys

from traceback_example import produce_exception

print('print_exc() with no exception:')
traceback.print_exc(file=sys.stdout)
print()

try:
    produce_exception()
except Exception as err:
    print('print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)

# In this example, the file handle for sys.stdout is substituted so the informational and traceback messages
# are mingled correctly:
#
# $ python3 traceback_print_exc.py
#
# print_exc() with no exception:
# NoneType: None
#
# print_exc():
# Traceback (most recent call last):
#   File "traceback_print_exc.py", line 20, in <module>
#     produce_exception()
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 19, in produce_exception
#     raise RuntimeError()
# RuntimeError
#
# print_exc(1):
# Traceback (most recent call last):
#   File "traceback_print_exc.py", line 20, in <module>
#     produce_exception()
# RuntimeError