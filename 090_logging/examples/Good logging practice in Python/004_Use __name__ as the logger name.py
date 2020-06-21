# It is not a requirement to set the logger name as __name__, but by doing that, it brings us some benefits.
# In case if you dont know, the variable __name__ is the current module name in Python. For example,
# you write this in a module foo.bar.my_module:
#
logger.getLogger(__name__)

# Its actually the same as this:
#
# logger.getLogger("foo.bar.my_module")
# Since the Python's logging configuration system follows a hierarchy design, the levels in the hierarchy are separated
# by dots, just like Python's package and module names. Given foo.bar.my_module as the logger name, the hierarchy will
# be:
#
# + foo
#   + bar
#     - my_module
# Say we have many logger names like these
#
# foo.bar.my_module
# foo.bar.my_module2
# foo.eggs.spam
# foo.eggs.spam2
# Then the corresponding hierarchy will be:
#
# + foo
#   + bar
#     - my_module
#     - my_module2
#   + eggs
#     - spam
#     - spam2
# With that, say you want to configure the loggers for all modules under a package, it can be done easily
# by configuring the logger with the package as the name. For example, you notice that the log messages from the modules
# in the foo.eggs package are too verbose, you want to filter most of them out. With the configuration hierarchy,
# you can configure foo.eggs package to a higher logging level, say WARNING. In this way, for the logs messages from
#
# foo.eggs.spam
# foo.eggs.spam2
# as long as their logging level is not equal or higher than WARNING, they will not be processed by the handler.
#
# Besides you can control the logger for the whole package, by using __name__ as the logger name you can also configure
# the formatter to output the logger name. Its very helpful to know which module is writing the log.