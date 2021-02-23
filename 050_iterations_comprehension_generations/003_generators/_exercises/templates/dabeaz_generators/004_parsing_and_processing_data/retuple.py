# # retuple.py
# #
# # Read a sequence of log lines and parse them into a sequence of tuples
#
# loglines = o.. *a..
#
# ______ __
#
# logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
#            r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'
#
# logpat   = __.co..?
#
# # line, g
# groups   = ?.m.. ? ___ ? __ ?
# tuples   = ?.gr.. ___ ? __ gr.. __ ?
#
# __ __name__ __ '__main__'
# # t
#     ___ ? __ tu..
#         print ?
