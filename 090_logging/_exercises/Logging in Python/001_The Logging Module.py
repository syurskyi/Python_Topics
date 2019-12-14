# The Logging Module
# The l____ module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as
# well as enterprise teams. It is used by most of the third-party Python libraries, so you can integrate your log
# messages with the ones from those libraries to produce a homogeneous log for your application.
#
# Adding l____ to your Python program is as easy as this:

______ l____
# With the l____ module imported, you can use something called a logger to log messages that you want to see.
# By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be
# used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
# The l____ module provides you with a default logger that allows you to get started without needing to do much
# configuration. The corresponding methods for each level can be called as shown in the following example:

______ l____

l____.debug('This is a debug message')
l____.info('This is an info message')
l____.warning('This is a warning message')
l____.error('This is an error message')
l____.critical('This is a critical message')

# The output of the above program would look like this:
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# The output shows the severity level before each message along with root, which is the name the l____ module gives
# to its default logger. (Loggers are discussed in detail in later sections.) This format, which shows the level, name,
# and message separated by a colon (:), is the default output format that can be configured to include things
# like timestamp, line number, and other details.
#
# Notice that the debug() and info() messages didnt get logged. This is because, by default, the l____ module logs
# the messages with a severity level of WARNING or above. You can change that by configuring the l____ module to
# log events of all levels if you want. You can also define your own severity levels by changing configurations,
# but it is generally not recommended as it can cause confusion with logs of some third-party libraries that you
# might be using.