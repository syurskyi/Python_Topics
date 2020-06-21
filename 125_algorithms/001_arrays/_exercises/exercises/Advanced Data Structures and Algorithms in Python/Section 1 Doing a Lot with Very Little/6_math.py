# ___ square_free n
#
#     count _ 0
#     ___ i __ ra.. 1, ?+1
#         ok _ T..
#         ___ j __ ra.. 2 ?
#             __ i % (j*j) __ 0
#                 ok _ F..
#                 b..
#         __ o.
#             c.. +_ 1
#
#     r_ ?
#
# ___ inclusion_exclusion n
#     primes _ [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#
#     ___ count k primes_used
#         __ k __ le. p..
#             product _ 1
#             ___ p __ p_u..
#                 ? *_ p * p
#             __ le. p_u.. % 2 __ 0
#                 r_ ? // p..
#             r_ - ? // p..
#
#         r_ co.. k + 1 p_u.. + \
#                co.. k + 1 p_u.. + |p..|k
#
#     r_ ? 0 ||   # list
#
# ___ i __ ra.. 1 10000
#     sf _ s_f.. ?
#     ie _ i_e.. ?
#     #print(i, sf, ie)
#     # supposed to fail at some point, depending on how many primes you have
#     ass.. sf __ ie, 'i_@, sf_@, ie_@'.f.. ? ? ?