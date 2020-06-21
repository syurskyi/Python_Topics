# The trace hook can return a new hook to be used inside the new scope (the local trace function). It is possible,
# for instance, to control tracing to only run line-by-line within certain modules or functions.

# !/usr/bin/env python
# encoding: utf-8

import sys


def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print '  %s line %s' % (func_name, line_no)


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    return


def c(input):
    print 'input =', input
    print 'Leaving c()'


def b(arg):
    val = arg * 5
    c(val)
    print 'Leaving b()'


def a():
    b(2)
    print 'Leaving a()'


TRACE_INTO = ['b']

sys.settrace(trace_calls)
a()

# Here the global list of functions is kept in the variable TRACE_INTO, so when trace_calls() runs it can return
# trace_lines() to enable tracing inside of b().

# $ python sys_settrace_line.py
#
# Exception TypeError: "argument of type 'NoneType' is not iterable" in <function _remove at 0x1004479b0> ignored
# Call to a on line 40 of sys_settrace_line.py
# Call to b on line 35 of sys_settrace_line.py
#   b line 36
#   b line 37
# Call to c on line 31 of sys_settrace_line.py
# input = 10
# Leaving c()
#   b line 38
# Leaving b()
# Leaving a()
# Call to _remove on line 38 of /Users/dhellmann/Envs/pymotw/bin/../lib/python2.7/_weakrefset.py