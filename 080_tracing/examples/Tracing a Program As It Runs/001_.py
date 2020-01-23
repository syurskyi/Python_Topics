# There are two ways to inject code to watch a program run: tracing and profiling. They are similar, but intended for
# different purposes and so have different constraints. The easiest, but least efficient, way to monitor a program is
# through a trace hook, which can be used for writing a debugger, code coverage monitoring, or many other purposes.
#
# The trace hook is modified by passing a callback function to sys.settrace(). The callback will receive
# three arguments, frame (the stack frame from the code being run), event (a string naming the type of notification),
# and arg (an event-specific value). There are 7 event types for different levels of information that occur as
# a program is being executed.
#
# Event	When	arg value
# 'call'	Before a function is executed.	None
# 'line'	Before a line is executed.	None
# 'return'	Before a function returns.	The value being returned.
# 'exception'	After an exception occurs.	The (exception, value, traceback) tuple.
# 'c_call'	Before a C function is called.	The C function object.
# 'c_return'	After a C function returns.	None
# 'c_exception'	After a C function throws an error.	None