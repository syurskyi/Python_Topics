
# In Python 3.0 (and 2.6 for compatibility):
def func(a, b, c, d):
    x = 1
    y = 2

code = func.__code__                     # Code object of function object
print(code.co_nlocals)
# 6
print(code.co_varnames)                        # All local var names
# ('a', 'b', 'c', 'd', 'x', 'y')
print(code.co_varnames[:code.co_argcount])     # First N locals are expected args
# ('a', 'b', 'c', 'd')

import sys                               # For backward compatibility
print(sys.version_info)                         # [0] is major release number
# (3, 0, 0, 'final', 0)
code = func.__code__ if sys.version_info[0] == 3 else func.func_code