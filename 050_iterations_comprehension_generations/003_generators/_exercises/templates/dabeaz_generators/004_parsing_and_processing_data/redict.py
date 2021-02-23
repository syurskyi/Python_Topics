# # redict.py
# #
# # Read a sequence of log lines and parse them into a sequence of dictionaries
#
# loglines _ o.. *a..
#
# ______ __
#
# logpats  _ r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
#            r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'
#
# logpat   _ __.co.. ?
#
# # line, g
# groups   _ ?.m.. ? ___ ? __ l_l_
# tuples   _ ?.gr.. ___ ? __ gr.. __ ?
#
# colnames _ ('host','referrer','user','datetime',
#             'method', 'request','proto','status','bytes')
#
# # t
# log      _ di__ z.. ? ? ___ ? __ tu..
#
# __ __name__ __ '__main__'
# # x
#     ___ ? __ ?
#         print ?
