# ______ n.. __ np
#
# ___ run_recursive array
#     ___ inner line col
#         __ l.. < 0 o. c.. < 0
#             r_ 10**20
#         __ l.. __ 0 an. co. __ 0
#             r_ a..|?
#         r_ a..|l.. c..| + mi. i.. l.. - 1 c..
#                                       i.. l.. c.. - 1
#
#     n _ a__.s..|0
#     r_ i.. ? - 1 ? - 1
#
#
# ___ print_path dp array line col
#     prev_dp _ d.|l.. c.. - a..|l.. c..
#     __ c.. - 1 >_ 0 an. p_d. __ d.|l.. c.. - 1
#         p_p.. d. a.. l c.. - 1
#     ____ l.. - 1 >_ 0 an. p_d. __ d.|l.. - 1 c..
#         p_p.. d. a.., l.. - 1 c..
#     print l.. c..
#
#
# ___ run_dp array
#     dp _ __.z_l.. ?
#     n _ ?.s..|0
#     d.|0, 0 _ ?|0, 0
#     ___ i __ ra.. 1 n
#         d.|0 ? _ d.|0 ? - 1 + ?|0 ?
#         d.|? 0 _ d.|? - 1 0 + ?|? 0
#     ___ i __ ra.. 1 n
#         ___ j __ ra.. 1 n
#             d.|? ? _ ?|? ? + mi. d.|? - 1 ?| d.|? ? - 1
#     print_path d. ? n - 1 n - 1
#     r_ d.|n - 1, n - 1
#
#
# ___ run_dp_memory_optimized array
#     dp1 _ __.z_l.. ?|0
#     dp2 _ __.z_l..?|0
#     n _ __1.s..|0
#     __1|0 _ ?|0 0
#     ___ i in range(1, n):
#         __1|? _ __1|? - 1 + ?|0 ?
#     ___ i __ ra.. 1 n
#         __2|0 _ __1|0 + ?|? 0
#         ___ j __ ra.. 1 n
#             __2|? _ ?|? ? + mi. __1|? __2|? - 1
#         __1|; _ __2
#     r_ __1|n - 1
#
#
# array _ __.a..||
#     [4, 3, 4, 31],
#     [1, 15, 9, 11],
#     [71, 13, 10, 6],
#     [21, 41, 51, 2]
# ||
#
# print('Recursive:', r_r.. ?
# print('DP:', r_d. ?
# print('Memory optimized DP:', r_d_m_o.. ?
