# Another useful way to use the hooks is to keep up with which functions are being called, and what their return values
# are. To monitor return values, watch for the return event.

#!/usr/bin/env python
# encoding: utf-8

import sys

def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
        return trace_calls_and_returns
    elif event == 'return':
        print '%s => %s' % (func_name, arg)
    return

def b():
    print 'in b()'
    return 'response_from_b '

def a():
    print 'in a()'
    val = b()
    return val * 2

sys.settrace(trace_calls_and_returns)
a()

# The local trace function is used for watching returns, so trace_calls_and_returns() needs to return a reference
# to itself when a function is called, so the return value can be monitored.

# $ python sys_settrace_return.py
#
# Call to a on line 25 of sys_settrace_return.py
# in a()
# Call to b on line 21 of sys_settrace_return.py
# in b()
# b => response_from_b
# a => response_from_b response_from_b
# Call to _remove on line 38 of /Users/dhellmann/Envs/pymotw/bin/../lib/python2.7/_weakrefset.py
# Call to _remove on line 38 of /Users/dhellmann/Envs/pymotw/bin/../lib/python2.7/_weakrefset.py

