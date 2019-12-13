# Capture exceptions with the traceback
# While its a good practice to log a message when something goes wrong, but it won’t be helpful if there is no
# traceback. You should capture exceptions and record them with traceback. Following is an example:

try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception as exception:
    logger.error('Failed to open file', exc_info=True)
    
# By calling logger methods with exc_info=True parameter, the traceback will be dumped to the logger. As you can see the result
#
# ERROR:__main__:Failed to open file
# Traceback (most recent call last):
#   File "example.py", line 6, in <module>
#     open('/path/to/does/not/exist', 'rb')
# IOError: [Errno 2] No such file or directory: '/path/to/does/not/exist'
# Since Python 3.5, you can also pass the exception instance to exc_info parameter. Besides exc_info parameter, you can also call logger.exception(msg, *args), it is the same as calling to logger.error(msg, *args, exc_info=True).