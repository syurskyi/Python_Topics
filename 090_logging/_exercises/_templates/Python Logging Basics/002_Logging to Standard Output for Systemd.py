# # This is the simplest and probably the best option for configuring logging these days. When using systemd to run
# # a daemon, applications can just send log messages to stdout or stderr and have systemd forward the messages
# # to journald and syslog. As an additional perk, this does not even require catching exceptions, as Python already
# # writes those to standard error. That said, follow proper convention and handle your exceptions.
# #
# # In the case of running Python in containers like Docker, logging to standard output is also often the easiest move
# # as this output can be directly and easily managed by the container itself.
#
# ______ l____
# ______ __
#
# l____.bC_ le.. _ __.env__.ge. "LOGLEVEL", "INFO"
#
# # exit(main())
# # That is it. The application will now log all messages with level INFO or above to stderr, using a simple format:
# #
# # ERROR:the.module.name:The log message
# #
# # The application can even be configured to include DEBUG messages, or maybe only ERROR, by setting the LOGLEVEL
# # environment variable.
# # The only problem with this solution is that exceptions are logged as multiple lines, which can cause problems
# # for later analysis. Sadly, configuring Python to send multi-line exceptions as a single line is not quite as simple,
# # but certainly possible. Note the implementation here below, calling logging.exception is shorthand equivalent
# # to logging.error(..., exc_info=True).
#
# ______ l____
# ______ os
#
#
# c_ OneLineExceptionFormatter l____.F...
#     ___ formatException ____ exc_info
#         result _ s__.fE_ ?
#         r_ re.. ?
#
#     ___ format ____ record
#         result _ s__.fo.. ?
#         i_ r__.exc_text
#             result = ?.re.. "\n", ""
#         r_ ?
#
#
# handler _ l____.S_H_
# formatter = O... l____.B._F.
# h__.sF_ ?
# root = l____.gL_
# ?.sL_ __.env__.ge_ "LOGLEVEL", "INFO"
# ?.aH_ h...
#
# t__
#     ex.. m..
# e____ Exception:
#     l____.ex... "Exception in main(): "
#     ex.. 1
