# # genopen.py
# #
# # Takes a sequence of filenames as input and yields a sequence of file
# # objects that have been suitably open
#
# ______ gzip, bz2
#
# # # path
# ___ gen_open paths
#     ___ ? __ ?
#         __ ?.su.. __ *.gz
#             y... g__.o.. ? *rt
#         ____ ?.su.. __ *.bz2
#             y... bz2.o.. ? *rt
#         ____
#             y... o.. ? *rt
#
# # Example use
#
# # # f
# __ __name__ __ '__main__':
#     f.. p_l_ ______ P..
#     lognames = P.. *www .r_g_ *access-log*
#     logfiles = g.. ?
#     ___ f __ ?
#         print ?
