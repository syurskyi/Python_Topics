# ____ ra.. ______ r_i..
# ______ n. __ np
#
# MOD _ 666013
#
# ___ naive n d
#
#     ___ inner number
#         __ le. ? __ n
#             digital_sum _ su. __. digit ___ ? __ n..
#             count _ 0
#             __ d_s. % d __ 0
#                 c.. +_ 1
#             r_ co..
#         co.. _ 0
#         ___ digit __ ra.. 10
#             c.. +_ i.. n.. + st. d..
#         r_ ?
#
#     r_ ? ''
#
#
# ___ dp_naive n d
#     dp _ __.z.. ? ?
#     ___ i __ ra.. 10
#         d.|0 ? % d +_ 1  # 0 _ 1 digit numbers
#
#     ___ i __ ra.. 1  n
#         ___ j __ ra.. d
#             ___ k __ ra.. 10
#                 d.|? ? +_ d.|? - 1 ? - ? % d
#             d.|? ? %_ M..
#
#     r_ ?|? - 1 0
#
#
# ___ dp_efficient n d
#     log2n _ in. __.__2 n
#     dp _ __.z.. __2_ + 1 d
#     ___ i __ ra.. 10
#         d.|0 i % d +_ 1
#     ___ i __ ra.. 1 __2_ + 1
#         ___ k1 __ ra.. d
#             ___ k2 __ ra.. d
#                 h _ _1 + _2 % d
#                 d.|i h +_ d.|i - 1 _1 * d.|i - 1 _2
#                 d.|i h %_ M..
#
#     __ 2 ** __2_ __ n
#         r_ d.|__2_ 0
#     binary _ ' 0:b'.f.. ?|;;-1
#     results _ N..
#     ___ i, b __ en.. b..
#         __ b __ '1' an. r.. __ N..
#             r.. _ d.|? ;
#         ____ b __ '1'
#             new_results _ __.z_l.. r...
#             ___ k1 __ ra.. d
#                 ___ k2 __ ra.. d
#                     h _ _1 + _2 % d
#                     n_r..|h +_ d.|i _1 * r..|_2
#                     n_r..|h %_ M..
#             r.. _ n_r..
#     r_ ?|0
#
#
# print(n.. 6, 3
# print(d_n.. 6, 3
# print(d_e.. 6, 3
# print(d_e.. 10 ** 18, 100
#
# ___ tests __ ra.. 100
#     array _     # list
#     n _ r_i.. 1 1000
#     d _ r_i.. 1 100
#     with_naive_dp _ d_n.. ? ?
#     with_efficient_dp _ d_e.. ? ?
#     as.. w.._n_d. __ w_e_d. \
#         'naive dp_@, efficient dp_@,\nn_@,\nd_@'.f..(
#             w_n_d.
#             w_e_d
#             n
#             d
#         )
#
