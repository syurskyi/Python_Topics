# #
# # Asyncio.loop - Section 4 Asynchronous Programming
# #
#
#
# ______ a..
# ______ d_t_
# ______ ti..
#
# ___ function_1 end_time loop
#     print ("function_1 called")
#     print ?
#     __ (l__.t__ + 1.0) < ?
#         l__.c_l.. 1 _2, e.. l__
#     ____
#         l__.s..
#
# ___ function_2 end_time loop
#     print ("function_2 called ")
#     print e..
#     __ (l__.t__ + 1.0) < e..
#         l__.c_l.. 1 _3 e.. l__
#     ____
#         l__.s..
#
# ___ function_3 end_time loop
#     print ("function_3 called")
#     print e..
#     __ l__.t__ + 1.0| < e..
#         l__.c_l.. 1 _1 e.. l__
#     ____
#         l__.s..
#
# ___ function_4 end_time loop
#     print ("function_5 called")
#     print e..
#     __ l__.t__ + 1.0| < e..
#         l__.c_l.. 1 _4, e.. l__
#     ____
#         l__.s..
#
# loop _ ?.g_e_l..
#
# # Schedule the first call to display_date()
# end_loop_1 _ l__.t__ + 9.0
# l__.c_s.. _1, e_1 l__
# #loop.call_soon(function_4, end_loop_1, loop)
#
# # Blocking call interrupted by loop.stop()
# l__.r_f..
# l__.c..
