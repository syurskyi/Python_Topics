# Exceptions can be monitored by looking for the exception event in a local trace function. When an exception occurs,
# the trace hook is called with a tuple containing the type of exception, the exception object, and a traceback object.

# !/usr/bin/env python
# encoding: utf-8

import sys


def trace_exceptions(frame, event, arg):
    if event != 'exception':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    exc_type, exc_value, exc_traceback = arg
    print 'Tracing exception: %s "%s" on line %s of %s' % \
          (exc_type.__name__, exc_value, line_no, func_name)


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name in TRACE_INTO:
        return trace_exceptions


def c():
    raise RuntimeError('generating exception in c()')


def b():
    c()
    print 'Leaving b()'


def a():
    b()
    print 'Leaving a()'


TRACE_INTO = ['a', 'b', 'c']

sys.settrace(trace_calls)
try:
    a()
except Exception, e:
    print 'Exception handler:', e

# Take care to limit where the local function is applied because some of the internals of formatting error messages
# generate, and ignore, their own exceptions. Every exception is seen by the trace hook, whether the caller catches
# and ignores it or not.

# $ python sys_settrace_exception.py
#
# Exception TypeError: "argument of type 'NoneType' is not iterable" in <function _remove at 0x1004479b0> ignored
# Tracing exception: RuntimeError "generating exception in c()" on line 26 of c
# Tracing exception: RuntimeError "generating exception in c()" on line 29 of b
# Tracing exception: RuntimeError "generating exception in c()" on line 33 of a
# Exception handler: generating exception in c()

