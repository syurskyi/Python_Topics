# You can use the basicConfig(**kwargs) method to configure the logging:
#
# You will notice that the logging module breaks PEP8 styleguide and uses camelCase naming conventions.
# This is because it was adopted from Log4j, a logging utility in Java. It is a known issue in the package but by
# the time it was decided to add it to the standard library, it had already been adopted by users and changing it
# to meet PEP8 requirements would cause backwards compatibility issues. (Source)
#
# Some of the commonly used parameters for basicConfig() are the following:
#
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.
# By using the level parameter, you can set what level of log messages you want to record.
# This can be done by passing one of the constants available in the class, and this would enable all logging calls at
# or above that level to be logged. Here s an example:
#
______ l____

l____.basicConfig(level=l____.DEBUG)
l____.debug('This will get logged')
# DEBUG:root:This will get logged

# All events at or above DEBUG level will now get logged.
# Similarly, for logging to a file rather than the console, filename and filemode can be used, and you can decide
# the format of the message using format. The following example shows the usage of all three:
#
______ l____

l____.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
l____.warning('This will get logged to a file')
# root - ERROR - This will get logged to a file

# The message will look like this but will be written to a file named app.log instead of the console.
# The filemode is set to w, which means the log file is opened in write mode each time basicConfig() is called,
# and each run of the program will rewrite the file. The default configuration for filemode is a, which is append.
# You can customize the root logger even further by using more parameters for basicConfig(), which can be found here.
#
# It should be noted that calling basicConfig() to configure the root logger works only if the root logger has not been
# configured before. Basically, this function can only be called once.
#
# debug(), info(), warning(), error(), and critical() also call basicConfig() without arguments automatically if it has
# not been called before. This means that after the first time one of the above functions is called, you can no longer
# configure the root logger because they would have called the basicConfig() function internally.
#
# The default setting in basicConfig() is to set the logger to write to the console in the following format:
#
# ERROR:root:This is an error message