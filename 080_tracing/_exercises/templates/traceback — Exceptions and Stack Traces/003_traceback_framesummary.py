# The StackSummary is an iterable container holding FrameSummary instances.

# traceback_framesummary.py
import traceback
import sys

from traceback_example import call_function

template = (
    '{fs.filename:<26}:{fs.lineno}:{fs.name}:\n'
    '    {fs.line}'
)


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    for fs in summary:
        print(template.format(fs=fs))


print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
call_function(f)

# Each FrameSummary describes a frame of the stack, including information about where in the program source files the execution context is.
#
# $ python3 traceback_framesummary.py
#
# Calling f() directly:
# traceback_framesummary.py :23:f:
#     traceback.walk_stack(None)
# traceback_framesummary.py :30:<module>:
#     f()
#
# Calling f() from 3 levels deep:
# traceback_framesummary.py :23:f:
#     traceback.walk_stack(None)
# .../traceback_example.py:26:call_function:
#     return f()
# .../traceback_example.py:24:call_function:
#     return call_function(f, recursion_level - 1)
# .../traceback_example.py:24:call_function:
#     return call_function(f, recursion_level - 1)
# traceback_framesummary.py :34:<module>:
#     call_function(f)
