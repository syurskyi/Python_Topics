# The traceback module works with the call stack to produce error messages. A traceback is a stack trace from the point
# of an exception handler down the call chain to the point where the exception was raised. You can also work with
# the current call stack up from the point of a call (and without the context of an error), which is useful for
# finding out the paths being followed into a function.
#
# The functions in traceback fall into several common categories. There are functions for extracting raw tracebacks
# from the current runtime environment (either an exception handler for a traceback, or the regular stack).
# The extracted stack trace is a sequence of tuples containing the filename, line number, function name, and text
# of the source line.
#
# Once extracted, the stack trace can be formatted using functions like format_exception(), format_stack(), etc.
# The format functions return a list of strings with messages formatted to be printed. There are shorthand functions
# for printing the formatted values, as well.
#
# Although the functions in traceback mimic the behavior of the interactive interpreter by default,
# they also are useful for handling exceptions in situations where dumping the full stack trace to stderr
# is not desirable. For example, a web application may need to format the traceback so it looks good in HTML.
# An IDE may convert the elements of the stack trace into a clickable list that lets the user browse the source.