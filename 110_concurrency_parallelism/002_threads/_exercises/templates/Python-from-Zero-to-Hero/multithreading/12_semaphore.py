# _______ c__.f__
# _______ r__
# _______ _
# _______ t___
#
#
# ___ work semaphore
#     t___.s.  r__.r.. 5 10
#     print('Releasing 1 connection')
#     ?.r..
#
#
# ___ connect semaphore reached_max_connections
#     w___ c__.f__.T... m.._10 __ ex
#         w.... T..
#             connections_counter = 0
#             w.... n.. r__.i..
#                 print _*\nConnection n= ?
#                 s__.a..
#                 ? += 1
#
#                 ?.s.. w.. s..
#
#                 t___.s.. 0.8
#
#             t___.s.. 5
#
#
# ___ connections_guard semaphore reached_max_connections
#     w.... T..
#         print _*[guard] semaphore= s__._v..
#         t___.s.. 1.5
#
#         __ s__._v.. __ 0
#             r__.s..
#             print _*[guard] Reached max connections!')
#             t___.s.. 10
#             r__.c..
#
#
# __ _____ __ _____
#     max_connections = 10
#     reached_max_connections = _.E..
#
#     semaphore = _.S.. v.._m..
#     w___ c__.f__.T... m.._2 __ executor
#         e__.s.. c.. s.. r..
#         e__.s.. c.. s.. r..
