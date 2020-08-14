# # -*- coding: utf-8 -*-
#
# ______ ?  # docs:  https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# #    logging from multiple python modules:  https://docs.python.org/3/howto/logging.html#logging-from-multiple-modules
# #      also, see this :  https://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules
# ______ ?.handlers  # required for using additional handlers
# # import logging.config  # __ using a config file
#
#
# ___ singleton ___  # singleton, how to:  https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
#     instances _   3 dict
#     ___ get_instance
#         __ ___ no. __ ?
#             ?|___ _ ___
#         r_ ?|___
#     r_ ?
#
#
# ?s..
# c_ Logger
#     ___  -
#         """ Create a logger and attach some handlers with individual formatters.
#         """
#         # logging.config.fileConfig('logging.conf')  # __ using a config file
#         # self.logger = logging.getLogger('root')  # __ you want to use the (default) 'root' logger
#
#         # Create (a) logger  (this is different from the "root" logger, which I'm not gonna be using)
#         logger _ ?.gL..('mylog')  # name of the logger
#         ?.sL.. ?.D..  # set a "default" log level; individual handlers re-set this
#
#         # Stream handler (prints to STDOUT)
#         stream_handler _ ?.SH..
#         formatter_1 _ ?.F..
#             fmt_'_ a_t_ s | _ l.. .3s | _ m.. s'
#         )  # string format operations explanations:    https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
#         #       % start of formatter
#         #         () mapping key; to LogRecord attributes, see:  https://docs.python.org/3.4/library/logging.html#logrecord-attributes
#         #         .(dot) acts as "trim"
#         #         -(minus) is "left adjusted"
#         #         3 is the number of characters to apply effect
#         #       s signifies string (end of formatter)
#         #
#         #   # color in formatter (TODO):  https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
#         #
#         ?.sF.. ?
#         ?.sL.. ?.I..
#
#         # File handler (writes to a file)
#         logFilePath _ 'logging-example.log'
#         file_handler _ ?.h__.RHFH... ? m.._ _  # 'a' for append
#         formatter_2 _ ?.F..
#             fmt_'_ a_t_ s | _ n.. -20s | _ l.. -10s | _ m.. s'
#         )
#         ?.sF.. ?
#         ?.sL..?.D..  # DEBUG (plus all other levels) appear in .log file only.
#
#         # Attach handlers
#         ?.aH.. f..
#         ?.aH.. s..
