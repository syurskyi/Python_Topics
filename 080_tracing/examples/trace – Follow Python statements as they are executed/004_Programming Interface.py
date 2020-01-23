# For a little more control over the trace interface, you can invoke it from within your program using a Trace object.
# Trace lets you set up fixtures and other dependencies before running a single function or execing a Python command
# to be traced.

import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')

# Since the example only traces into the recurse() function, no information from main.py is included in the output.
#
# $ python trace_run.py
#
#  --- modulename: trace_run, funcname: <module>
# <string>(1):   --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(2)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(1)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(0)
# recurse.py(14):     if level:
# recurse.py(16):     return
# recurse.py(16):     return
# recurse.py(16):     return
# That same output could have been produced with the runfunc() method, too. runfunc() accepts arbitrary positional and
# keyword arguments, which are passed to the function when it is called by the tracer.

import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.runfunc(recurse, 2)

# $ python trace_runfunc.py
#
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(2)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(1)
# recurse.py(14):     if level:
# recurse.py(15):         recurse(level-1)
#  --- modulename: recurse, funcname: recurse
# recurse.py(13):     print 'recurse(%s)' % level
# recurse(0)
# recurse.py(14):     if level:
# recurse.py(16):     return
# recurse.py(16):     return
# recurse.py(16):     return