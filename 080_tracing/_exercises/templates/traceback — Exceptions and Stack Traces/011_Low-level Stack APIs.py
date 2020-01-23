# The extract_stack() function works like extract_tb().
#
# traceback_extract_stack.py

import sys
import os

from traceback_example import call_function

template = '{filename:<26}:{linenum}:{funcname}:\n    {source}'


def f():
    return traceback.extract_stack()


stack = call_function(f)
for filename, linenum, funcname, source in stack:
    if funcname != '<module>':
        funcname = funcname + '()'
    print(template.format(
        filename=os.path.basename(filename),
        linenum=linenum,
        source=source,
        funcname=funcname)
    )

# It also accepts arguments, not shown here, to start from an alternate place in the stack frame or to limit the depth of traversal.
#
# $ python3 traceback_extract_stack.py
#
# traceback_extract_stack.py:23:<module>:
#     stack = call_function(f)
# traceback_example.py      :24:call_function():
#     return call_function(f, recursion_level - 1)
# traceback_example.py      :24:call_function():
#     return call_function(f, recursion_level - 1)
# traceback_example.py      :26:call_function():
#     return f()
# traceback_extract_stack.py:20:f():
#     return traceback.extract_stack()