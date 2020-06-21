# ___ three_loops array
#
#     n _ le. ?
#     max_sum _ ? 0
#     ___ start __ ra.. ?
#         ___ end __ ra..  s.. ?
#             current_sum _ su. ? ?:?+1
#             __ ? > m_s..
#                 m_s.. _ c_s..
#
#     r_ ?
#
# ___ two_loops array
#
#     n _ le. ?
#     max_sum _ ? 0
#     ___ start __ ra.. n
#         current_sum _ 0
#         ___ end __ ra.. s.. ?
#             c_s.. +_ ?|?
#             __ c_s.. > m_s..
#                 m_s.. _ c_s..
#
#     r_ ?
#
# ___ one_loop array
#
#     n _ le. ?
#     max_sum _ ? 0
#     current_sum _ ? 0
#     ___ i __ ra.. 1 ?
#         current_sum _ ma.  c_s.. + a.. ? a.. ?
#         max_sum _ ma. m_s.. c_s..
#
#     r_  m_s..
#
# arr1 _ [3,4,-9,1,2]
# arr2 _ [1,2,3]
# arr3 _ [-1,-2,-3]
# ass.. three_loops(arr1) == two_loops(arr1)
# ass.. three_loops(arr2) == two_loops(arr2)
# ass.. three_loops(arr3) == two_loops(arr3)
# ass.. one_loop(arr1) == two_loops(arr1)
# ass.. one_loop(arr2) == two_loops(arr2)
# ass.. one_loop(arr3) == two_loops(arr3)
