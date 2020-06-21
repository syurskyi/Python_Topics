# ______ n.. __ np
# ____ ra.. ______ r_i..
#
#
# ___ naive_query array a b
#     r_ mi. a..|?;?+1
#
#
# ___ compute_rmq_table array
#     n _ le. ?
#     log2n _ __. __.log2 ?
#     dp _ __.z.. __2. + 1 ?
#     ?|0 ; _ a..
#     pow _ 1
#     ___ i __ ra.. 1 __2_ + 1
#         ___ j __ ra.. n
#             d.|? ? _ d.|? - 1 ?
#             __ j + po. < n
#                 d.|? ? _ mi. d.|? ? d.|? - 1 ? + po.
#         po. *_ 2
#     r_ ?
#
#
# ___ dp_query array a b dp
#     k _ in. __.log2 ?2 - ?1 + 1
#     r_ mi. d.|k a d.|k b - 2**k + 1
#
#
# ___ tests __ ra.. 100
#     array _ ||  # list
#     n _ r_i.. 1 1000)
#     ___ i __ ra.. ?
#         a__.ap.. r_i.. 1 1000
#
#     dp _ c_r_t.. a..
#     ___ _ __ ra.. 2000
#         a _ r_i.. 0 n - 1
#         b _ r_i.. a n - 1
#         with_naive _ n_q.. a.. a b
#         with_dp _ d_q.. a.. a b d.
#         as.. ? __ w_n.. \
#             'naive_@, efficient dp_@,\nn_@,\na_@\n_@\narray_@'.f..(
#                 w_n..
#                 w_d.
#                 n
#                 a
#                 b
#                 a..
#             )

