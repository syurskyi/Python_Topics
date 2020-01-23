# A call event is generated before every function call. The frame passed to the callback can be used to find out which
# function is being called and from where.

#!/usr/bin/env python
# encoding: utf-8

import sys

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    print 'Call to %s on line %s of %s from line %s of %s' % \
        (func_name, func_line_no, func_filename,
         caller_line_no, caller_filename)
    return

def b():
    print 'in b()'

def a():
    print 'in a()'
    b()

sys.settrace(trace_calls)
a()

# $ python sys_settrace_call.py
#
# Exception AttributeError: "'NoneType' object has no attribute 'f_lineno'" in <function _remove at 0x1004479b0> ignored
# Call to a on line 27 of sys_settrace_call.py from line 32 of sys_settrace_call.py
# in a()
# Call to b on line 24 of sys_settrace_call.py from line 29 of sys_settrace_call.py
# in b()