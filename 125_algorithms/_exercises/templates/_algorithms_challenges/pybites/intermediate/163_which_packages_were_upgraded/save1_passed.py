# ___ changed_dependencies old_reqs s.. new_reqs s.. __ l..
#     """Compare old vs new requirement multiline strings
#        and return a list of dependencies that have been upgraded
#        (have a newer version)
#     """
#     old    # dict
#     new    # dict
#     ___ entry __ o__.s...s..('\n'
#         x ?.s.. '=='
#         y    # list
#
#         ___ i __ ? 1 .s.. '.'
#             __ l.. ? __ 1
#                 y.a.. '0' + s.. ?
#             ____
#                 y.a.. s.. ?
#
#         o.. x 0 ''.j.. ?
#
#     ___ entry __ n__.s...s.. '\n'
#         x ?.s.. '=='
#         y    # list
#
#         ___ i __ ? 1 .s.. '.'
#             __ l.. ? __ 1
#                 y.a.. '0' + s.. ?
#             ____
#                 y.a.. s.. ?
#         N.. x 0 ''.j.. ?
#
#     output    # list
#     ___ k1, v1 __ o__.i..
#         ___ k2, v2 __ n__.i..
#             __ ? __ ?
#                 __ l.. _1 > l.. _2
#                     v1 v1 |l.. _2
#                     __ i.. _2 > i.. _1
#                         ?.a.. _1
#                 ____ l.. _2 > l.. _1
#                     v2 _2 |l.. _1
#                     __ i.. _2 > i.. _1
#                         ?.a.. _1
#                 ____ l.. _1 __ l.. _2
#                     __ i.. _2 > i.. _1
#                         ?.a.. _1
#
#     r.. ?