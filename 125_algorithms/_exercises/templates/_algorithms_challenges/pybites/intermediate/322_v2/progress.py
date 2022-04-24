# ____ d__ _______ d__
# ____ d__ _______ t..
#
#
# ___ ontrack_reading books_goal i.. books_read i..
#                     day_of_year i.. N.. __ b..
#
#     year d__.t...year
#     boy d__ ? 1, 1)
#     eoy d__ ? 12, 31)
#
#     __ day_of_year
#         today boy + t..(d.._?-1
#     ____
#         t.. d__.t..
#
#     days_left ? - ? .d..
#     books_left ? - ?
#
#     __ b.. > 0
#         # use current reading rate
#         read_rate b.. / ? - b.. .d..
#     ____
#         # otherwise assume a reasonable reading goal
#         read_rate b.. / 365
#
#     print _*?_ , ?_
#     r.. T.. __ b.. __ 0 ____ b.. / r.. <_ d..
