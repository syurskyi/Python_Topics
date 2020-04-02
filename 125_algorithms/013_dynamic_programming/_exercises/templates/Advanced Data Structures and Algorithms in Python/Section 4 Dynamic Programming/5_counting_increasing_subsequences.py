# ____ ra.. ______ r..i..
#
# ______ n.. __ np
#
#
# ___ first_dp array k
#     n _ le. ?
#     dp _ __.z.. ? k
#     ?|; 0 _ 1
#     ___ i __ ra.. n
#         ___ p __ ra.. ?
#             __ a..|? > a..|?
#                 ___ j __ ra.. 1 k
#                     d.|1 ?4 +_ d.|?2 j -1
#     r_ su. d.|; k - 1
#
#
# ___ second_dp array k
#     n _ le. ?
#     dp _ __.z.. n k
#     ?|; 0 _ 1
#     ___ j __ ra.. 1 k
#         num _ ||  # dict # num[v] _ how many subsequences of length j end with v
#         ___ i __ ra.. 1 n
#             __ a..|? - 1 __ n..
#                 n..|a..|? - 1 +_ d.|? - 1 ? - 1
#             ____
#                 n..|a...|? - 1 _ d.|? - 1 ? - 1
#
#             ___ p __ ra.. a..|i
#                 __ p __ n..
#                     d.| ? ? +_ n..|?
#     r_ su. d.|; k - 1
#
#
# ___ tests __ ra.. 1000
#     array _ ||  # list
#     ___ i __ ra.. r_i.. 20 100
#         ?.ap.. r_i.. 1 100
#     k _ r_i.. 5 20
#     with_first _ f_d. a.. k
#     with_second _ s_d. a.. k
#     as.. w_f.. __ w_s.. \
#         'first_@, second_@,\narray_@,\nk_@'.f..(
#             w_f..
#             w_s..
#             a..
#             k
#         )
