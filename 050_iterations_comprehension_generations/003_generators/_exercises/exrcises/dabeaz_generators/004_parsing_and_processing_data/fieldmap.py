# # fieldmap.py
# #
# # Take a sequence of dictionaries and remap one of the fields
#
# # d
# ___ field_map dictseq name func
#     ___ ? __ ?
#         ? n.. _ f.. ? n..
#         y... ?
#
# # Example
#
# __ __name__ __ '__main__':
#
#     loglines _ o.. *a..
#
#     ______ __
#
#     logpats  _ r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
#                r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'
#
#     logpat   _ __.co.. ?
#
# # line, g
#     groups   _  ?.m.. ? ___ ? __ l_l_
#     tuples   _  ?.gr.. ___ ? __ gr.. __ ?
#
#     colnames _ ('host','referrer','user','datetime',
#                 'method', 'request','proto','status','bytes')
#
# # t
#     log      _ di__ z.. ? ? ___ ? __ tu..
#
#     log      _ f.. ? *status in.
# # s
#     log      _ f.. ? *bytes
#                          l____ ? in. ? __ ? !_ '-' ____ 0
#
# # x
#     ___ ? __ ?
#         print ?
