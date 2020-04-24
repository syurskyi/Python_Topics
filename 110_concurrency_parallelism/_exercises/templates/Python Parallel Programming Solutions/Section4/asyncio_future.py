# """
# Asyncio.Futures -  Section 4 Asynchronous Programming
# """
# ______ a..
# ______ ___
#
# #SUM OF N INTEGERS
# ??.?
# ___ first_coroutinem future N
#     count _ 0
#     ___ i __ ra.. 1 ?+1
#         c.._c.. + ?
#     ? ? ?.s.. 3
#     f__.s_r..("first coroutine (sum of N integers) result = "\
#                       + st. c..
#
#
# #FACTORIAL(N)
# ??.?
# ___ second_coroutine future N
#     count _ 1
#     ___ i __ ra.. 2 ?+1
#         c.. *_ ?
#     ? ? ?.s.. 4
#     f__.s_r..("second coroutine (factorial) result = "\
#                       + st. c..
#
# ___ got_result future
#     print ?.r..
#
#
# __ _______ __ _______
#     N1 _ in. ___.a.. 1
#     N2 _ in. ___.a.. 2
#
#     loop _ ?.g_e_l..
#     future1 _ ?.F..
#     future2 _ ?.F..
#
#     tasks _ |
#         first_coroutine _1 _1
#         second_coroutine _2 _2
#
#     _1.a_d_c.. g_r..
#     _2.a_d_c.. g_r..
#
#     ?.r_u_c.. ?.w.. t..
#     ?.c..
