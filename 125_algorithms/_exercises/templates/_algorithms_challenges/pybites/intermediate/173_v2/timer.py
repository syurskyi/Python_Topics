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
#
#     values ?.s..
#
#     days seconds minutes hours 0
#     ___ value __ ?
#         v i.. ? __ ? -1 .i.. ____ i.. ? |-1
#         __ ? -1 .i.. o. ? -1 __ 's'
#             s.. v
#         ____ ? -1 __ 'd'
#             d.. v
#         ____ ? -1 __ 'h'
#             h.. v
#         ____ ? -1 __ 'm'
#             m.. v
#
#
#     t__ s.. + t.. h.._? s.._? m.._?d.._?
#
#
#     r.. _* t.. @ t__.s.. _Y-_m-_d _H|_M:_S

