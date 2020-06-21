# The logging module also allows you to capture the full stack traces in an application. Exception information
# can be captured if the exc_info parameter is passed as True, and the logging functions are called like this:

import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
# ERROR:root:Exception occurred
# Traceback (most recent call last):
#   File "exceptions.py", line 6, in <module>
#     c = a / b
# ZeroDivisionError: division by zero
# [Finished in 0.2s]
# If exc_info is not set to True, the output of the above program would not tell us anything about the exception,
# which, in a real-world scenario, might not be as simple as a ZeroDivisionError. Imagine trying to debug an error in
# a complicated codebase with a log that shows only this:
#
# ERROR:root:Exception occurred
# Here is a quick tip: if you are logging from an exception handler, use the logging.exception() method, which logs
# a message with level ERROR and adds exception information to the message. To put it more simply,
# calling logging.exception() is like calling logging.error(exc_info=True). But since this method always dumps exception
# information, it should only be called from an exception handler. Take a look at this example:

import logging

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
# ERROR:root:Exception occurred
# Traceback (most recent call last):
#   File "exceptions.py", line 6, in <module>
#     c = a / b
# ZeroDivisionError: division by zero
# [Finished in 0.2s]
# Using logging.exception() would show a log at the level of ERROR. If you dont want that, you can call any of
# the other logging methods from debug() to critical() and pass the exc_info parameter as True.