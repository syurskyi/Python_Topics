# Calling Relationships
# In addition to coverage information, trace will collect and report on the relationships between functions
# that call each other.
#
# For a simple list of the functions called, use --listfuncs:
#
# $ python -m trace --listfuncs trace_example/main.py
#
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
#
# functions called:
# filename: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py, modulename: trace, funcname: _unsettrace
# filename: trace_example/main.py, modulename: main, funcname: <module>
# filename: trace_example/main.py, modulename: main, funcname: main
# filename: trace_example/recurse.py, modulename: recurse, funcname: <module>
# filename: trace_example/recurse.py, modulename: recurse, funcname: recurse
# For more details about who is doing the calling, use --trackcalls.
#
# $ python -m trace --listfuncs --trackcalls trace_example/main.py
#
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
#
# calling relationships:
#
# *** /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py ***
#     trace.Trace.runctx -> trace._unsettrace
#   --> trace_example/main.py
#     trace.Trace.runctx -> main.<module>
#
# *** trace_example/main.py ***
#     main.<module> -> main.main
#   --> trace_example/recurse.py
#     main.<module> -> recurse.<module>
#     main.main -> recurse.recurse
#
# *** trace_example/recurse.py ***
#     recurse.recurse -> recurse.recurse