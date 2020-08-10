# # You can create a new logger using the logger.getLogger(name) method. If a logger with the same name exists,
# # then that logger will be used.
# #
# # While you can give pretty much any name to the logger, the convention is to use the __name__ variable like this:
# #
# ______ l____
# logger _ l____.gL_ -n
# ?.i.. 'my logging message'
# # But, why use __name__ as the name of the logger, instead of hardcoding a name?
# #
# # Because the __name__ variable will hold the name of the module (python file) that called the code. So, when used
# # inside a module, it will create a logger bearing the value provided by the module's __name__ attribute.
# # By doing this, if you end up changing module name (file name) in future, you dont have to modify the internal code.
# # Now, once you've created a new logger, you should remember to log all your messages using the new logger.info()
# # instead of the root's logging.info() method.
# #
# # Another aspect to note is, all the loggers have a built-in hierarchy to it.
# # What do I mean by that?
# #
# # For example, if you have configured the root logger to log messages to a particular file. You also have
# # a custom logger for which you have not configured the file handler to send messages to console or another log file.
# # In this case, the custom logger will fallback and write to the file set by the root logger itself.
# # Until and unless you configure the log file of your custom logger.
# # So what is a file handler and how to set one up?
