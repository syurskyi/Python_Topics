# ______ n.. __ __
#
# inf _ 10 ** 18
#
#
# ___ generate_d n
#     d _ __.z.. ?2 ?2 dtype_np.int64
#     ___ i __ ra.. ?2
#         ___ j __ ra.. ?+1, ?2
#             ?|? ? _ __.ra...r_i.. 1 1.
#             __ ?|? ? __ 0
#                 ?|? ? _ inf
#             ?|? ? _ d|? ?
#     r_ ?
#
#
# ___ brute_force n d
#
#     ___ inner current_node current_length visited_set
#         __ le. v.. __ ? - 1
#             r_ c_l.. + ?|c_n.. 0
#
#         best _ inf
#         ___ i __ ra.. 1 ?
#             __ i no. __ v..
#                 best _ mi. b.. i.. ?
#                                        c_l.. + ?|c_n.. ?
#                                        v.. | |?
#         r_ ?
#
#     r_ ? 0 0
#
#
# ___ run_dp n d
#     dp _ __.o.. 2 ** ? ? * inf
#     # dp[S, c] _ sum of the minimum sum tour that visits all cities
#     #            corresponding to the indexes of the set bits __ S [...]
#     # S _ 10011 _> 0, 1, 4
#     ___ c __ ra.. 1 n
#         ?|1 << ? ? _ ?|0 ? # 1 << 3 _> 1000
#
#     ___ S __ ra.. 2**? - 1 # 111...1110
#         ___ c __ ra.. 1 ?
#             __ S & |1 << ? !_ 0
#                 S_no_c _ S - |1 << ?
#                 ___ c1 __ ra.. 1 ?
#                     __ S & 1 << _1 !_ 0
#                         d.|S c _ mi. d.|S c d.[S_no_c _1 + ?|_1 c
#
#     final_state _ 2**? - 2
#     best _ in.
#     ___ c __ ra.. 1 ?
#         best _ mi. b.. ?|f.._s.. ?| + ?|? 0
#     r_ ?
#
#
#
# ___ i __ ra.. 10
#     n _ __.ra__.r__i.. 2 5
#     d _ g_d ?
#
#     print(d)
#     print('brute force search :', b.. n d
#     print('dynamic programming:', r_d. n d
#     print('-' * 20)
