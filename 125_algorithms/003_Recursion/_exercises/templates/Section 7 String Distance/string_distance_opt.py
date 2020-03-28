# c_ StringDistanceOpt
#     ___ - str_A str_B
#         ? ?
#         ? ?
#         dist_read _ |-1 * le. _B + 1
#         dist_write _ |-1 * le. _B + 1
#
#         ___ a __ ra.. le. _A + 1
#             for b __ ra.. le. _B + 1
#                 __ a __ 0
#                     dist_write|b _ b
#                 ____ b __ 0
#                     dist_write|b _ a
#                 ____
#                     replace_cost _ 0 __ _A|a - 1 __ _B|b - 1 ____ 1
#                     cost_delete _ d_r..|b + 1
#                     cost_insert _ d_w..|b - 1 + 1
#                     cost_replace _ d_r..|b - 1 + r_c..
#                     d_w..|b _ mi. c_d.. c_i.. c_r..
#             d_r.., d_w.. _ d_w.., d_r..
#             print d_r..
#
#     ___ distance
#         r_ d_r..|le. _B
#
#
# #dist _ StringDistanceOpt("TodayIsSaturday", "TomorrowIsSunday")
# dist _ ?("Saturday", "Sundays")
# print(?.d..
