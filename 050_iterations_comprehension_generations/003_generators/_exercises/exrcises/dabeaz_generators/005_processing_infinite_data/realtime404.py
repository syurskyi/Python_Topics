# # realtime404.py
# #
# # Print all 404 requests as they happen in the log
#
# f.. apachelog ______ apache_log
# f.. follow ______ follow
#
# logfile  = o.. *run/foo/access-log
# loglines = f.. ?
# log      = a.. ?
#
# # r
# r404 = ? ___ ? __ ? __ ? *status __ 404
#
# ___ ? __ ?
#     print ? *host ? *datetime ? *request
