# c_ StringDistanceTopDown
#     ___ - str_A str_B
#         ?  ?
#         ?  ?
#         dist _ |||| *  le. _A + 1
#         ___ i __ ra.. le. _A + 1
#             d..|i _ |-1 * le. _B| + 1
#
#     ___ distance
#             r_ _r le. _A le. _B
#
#     ___ distance_r a b
#         __ d..|a |b !_ -1
#             r_ d..|a |b
#         __ a __ 0
#             r_ b
#         __ b __ 0
#             r_ a
#         replace_cost _ 0 __ _A|a - 1 __ _B|b - 1 ____ 1
#
#         cost_delete _ _r a - 1, b) + 1
#         cost_insert _ _r a, b - 1) + 1
#         cost_replace _ _r a - 1, b - 1 + r_c..
#         min_cost _ mi. c_d.. c_i.. c_r..
#         d...|a |b _ m_c..
#         r_ min_cost
#
#
# #dist = StringDistanceTopDown("TodayIsSaturday", "TomorrowIsSunday")
# dist = ?("Saturday", "Sundays")
# print(?.d..
