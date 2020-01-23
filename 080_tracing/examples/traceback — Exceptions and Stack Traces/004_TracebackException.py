# The TracebackException class is a high-level interface for building a StackSummary while processing a traceback.

# traceback_tracebackexception.py
import traceback
import sys

from traceback_example import produce_exception

print('with no exception:')
exc_type, exc_value, exc_tb = sys.exc_info()
tbe = traceback.TracebackException(exc_type, exc_value, exc_tb)
print(''.join(tbe.format()))

print('\nwith exception:')
try:
    produce_exception()
except Exception as err:
    exc_type, exc_value, exc_tb = sys.exc_info()
    tbe = traceback.TracebackException(
        exc_type, exc_value, exc_tb,
    )
    print(''.join(tbe.format()))

    print('\nexception only:')
    print(''.join(tbe.format_exception_only()))

# The format() method produces a formatted version of the full traceback, while format_exception_only() shows only
# the exception message.
#
# $ python3 traceback_tracebackexception.py
#
# with no exception:
# None: None
#
#
# with exception:
# Traceback (most recent call last):
#   File "traceback_tracebackexception.py", line 22, in <module>
#     produce_exception()
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 17, in produce_exception
#     produce_exception(recursion_level - 1)
#   File ".../traceback_example.py", line 19, in produce_exception
#     raise RuntimeError()
# RuntimeError
#
#
# exception only:
# RuntimeError