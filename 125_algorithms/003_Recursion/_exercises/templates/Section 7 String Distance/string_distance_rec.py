# c_ StringDistance
#     ___ - str_A str_B
#         ? ?
#         ? ?
#
#     ___ distance
#         r_ _r le. _A le. _B
#
#     ___ distance_r a b
#         __ a __ 0
#             r_ b
#         __ b __ 0
#             r_ a
#         replace_cost = 0 __ _A|a - 1 __ _B|b - 1 ____ 1
#
#         cost_delete = _r a - 1, b + 1
#         cost_insert = _r a, b - 1 + 1
#         cost_replace = _r(a - 1, b - 1) + r_c..
#         r_ min c_d.. c_i.. c_r..
#
#
# #dist = StringDistance("TodayIsSaturday", "TomorrowIsSunday")
# dist = ?("Saturday", "Sundays")
# print(?.d..
