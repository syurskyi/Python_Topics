# """
# In its simplest term, the `logging` module is used to print things out (to the console or to a file).
#
# The `logging` module should be used to communicate with the developer
# (e.g. information about what’s happening; when an error happens; a critical problem; etc…).
#
# To communicate with the user, continue using `print()` and `input()`.
#
# To use logging, we just have to import the `logging` module and get a new logger:
# """
#
# ______ ?
#
# logger _ ?.gL.. test_logger
#
# ?.i.. "This won't show up.
# ?.w.. This will.
#
# """
# There are various logging levels (below in ascending order of criticality),
# for you to use depending on the circumstance:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#
# So if you’re logging for help while developing or debugging, use the `DEBUG` level (`logger.debug('message')`).
#
# If your program’s about to crash because a critical exception happened; use `logger.critical()`.
#
# You can configure the output so all messages are shown, not just warning and above:
# """
#
# ?.bC.. l.._?.D..
#
# """
# You can configure the output to include more than just the level and the logger used. You can add for example the time:
# """
#
# ?.bC.. f.._'_(a_t..)_ _(l_n..)_:_(m..)_', l.._?.D..
#
# """
# Or below, an example of a great way to configure your logger for maximum readability and usefulness.
#
# Of course, as you go through your Python journey you may encounter situations where using a differently-configured
# logger would be better. Or when you’ll work with people who want logging in a particular way.
#
# You’ll then have to decide how you want to log things, and as most things in software that should be a team decision.
# """
#
# ______ ?
#
# ?.bC..(f.._'_(a_t..)_ _(l_n..)-8_ [_(f_n..)_:_(l..)d] _(m..)_'
#     datefmt_'%d-%m-%Y:%H:%M:%S',
#     l.._?.D..
#
# logger _ ?.gL.. my_app
# ?.d.. This is a debug log
# ?.i.. This is an info log
# ?.c.. This is critical
# ?.e.. An error occurred
#
# """
# And if you wanted your applications logs to go to a file instead of the console, do something like this:
# """
#
# ?.bC.. f.._'_(a_t..)_ _(l_n..)-8_ [_(f_n..)_:_(l..)d] _(m..)_'
#     datefmt_'%d-%m-%Y:%H:%M:%S'
#     l.._?.D..
#     f.._ logs.txt
#
# """
# If you call `logging.getLogger('my_app')` from many different files, you’ll always get the same `Logger`
# object—so any configuration changes and the handler added will be reflected throughout all the app.
#
# If you want to use a different name but want the configuration to be kept between handlers,
# the best way is to create child handlers:
# """
#
# ______ ?
#
# ?.bC.. f.._'_(a_t_)_ _(l_n..)-8_ [_(f_n..)_:_(l..)d] _(m..)_'
#     datefmt_'%d-%m-%Y:%H:%M:%S'
#     l.._?.D..
#     f_n.._logs.txt
#
# logger _ ?.gL.. my_app
#
# another_? _ ?.gL.. my_app.database  # gets a child logger called 'database' of 'my_app'
#
# """
# Add logging to your projects moving forward! It’s great when you can trace what was happening in your system as
# it happened with extensive logs (although, it does mean the code will be longer since you need to include logging
# statements everywhere).
# """