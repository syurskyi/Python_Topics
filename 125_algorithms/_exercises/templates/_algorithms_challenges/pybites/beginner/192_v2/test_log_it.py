# _______ l___
#
# _______ p__
#
# ____ ? _______ CRITICAL, DEBUG, ERROR, INFO, WARNING, log_it
#
# LOG_LEVEL
#     d.. ?
#     i.. ?
#     w.. ?
#     e.. ?
#     c.. ?
#
#
#
# ___ test_callable_log_levels
#     ___ level __ ?
#         ... c.. ? ?
#
#
# ?p__.m__.p.
#     "msg, level",
#     [
#         ("This is a debug message", "debug"),
#         ("This is an info message", "info"),
#         ("This is a warning message", "warning"),
#         ("This is an error message", "error"),
#         ("This is a critical message", "critical"),
#     ],
#
# ___ test_log_it msg level caplog
#     caplog.s.. l___.D..
#     ? ? ? m..
#     ... l.. c__.r.. __ 1
#     ___ record __  c__.r..
#         ...  r__l.. __ ?.u..
#         ...  r__m.. __ ?
#         ...  r__n.. __ pybites_logger
#
#
# ___ test_wrong_log_level caplog
#     msg  This is a warning message
#     ?.s.. l___.E..
#     ? ? ?
#     ... l.. c__.r.. __ 0
#
#     c__.s.. l___.E..
#     msg  This is an error message
#     ? ? ?
#     ... l.. c__.r.. __ 1
#     ___ record __  c__.r..
#         ...  r__l.. __ ERROR
#         ...  r__m.. __ ?
#         ...  r__n.. __ pybites_logger