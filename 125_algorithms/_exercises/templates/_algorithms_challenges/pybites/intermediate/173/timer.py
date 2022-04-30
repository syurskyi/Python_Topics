# ____ d__ _______ d__, t..
# _______ __
#
# NOW d__ y.._2019,  m.._2,  d.._6,
#                h.._22, m.._0 s.._0
#
#
# ___ add_todo delay_time s.. task s..
#              start_time d__ N.. __ s..
#     """
#     Add a todo list item in the future with a delay time.
#
#     Parse out the time unit from the passed in delay_time str:
#     - 30d = 30 days
#     - 1h 10m = 1 hour and 10 min
#     - 5m 3s = 5 min and 3 seconds
#     - 45 or 45s = 45 seconds
#
#     Return the task and planned time which is calculated from
#     provided start_time (here default = NOW):
#     >>> add_todo("1h 10m", "Wash my car")
#     >>> "Wash my car @ 2019-02-06 23:10:00"
#     """
#
#     days, hours, minutes, seconds 0, 0, 0, 0
#
#     #if delay_time.find(" ") > 0:
#     ___ unit __ ?.s.. " "
#         last_char ? -1
#         __ ? __ "d"
#             days i.. ? |-1
#         ____ l.. __ "h"
#             hours i.. ? |-1
#         ____ ? __ "m"
#             minutes i.. ? |-1
#         ____ ? __ "s"
#             seconds i.. ? |-1
#         ____ ?.i..
#             seconds i.. ?
#         ____
#             _____
#
#     r.. _* t.. @ s.. + t.. d.._? h.._? m.._? s.._?
#
#
# __ _______ __ _______
#     print ? "30", "test"