# # apachelog.py
# #
# # Parse an apache log file into a sequence of dictionaries
#
# f.. fieldmap ______ field_map
#
# ______ re
#
# logpats  _ r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
#            r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'
#
# logpat   _ re.co.. ?
#
# # # line, g
# ___ apache_log lines
#     groups _ ?.m.. ? ___ ? __ ?
#     tuples _  ?.gr.. ___ ? __ gr.. __ ?
#
#     colnames _ ('host','referrer','user','datetime',
#                 'method', 'request','proto','status','bytes')
#
# # t, s
#     log      _ di__(z.. ? ? ___ ? __ t..
#     log      _ f_m.. ? *status in.
#     log      _ f_m.. ? *bytes
#                          l____ ? in. ? __ ? !_ '-' ____ 0
#
#     r_ ?
#
# # Example use:
#
# # r
# __ __name__ __ '__main__':
#     f.. linesdir ______ lines_from_dir
#     lines _ ? *access-log* *www
#     log _ ? ?
#     ___ ? __ ?
#         print ?
#
#
