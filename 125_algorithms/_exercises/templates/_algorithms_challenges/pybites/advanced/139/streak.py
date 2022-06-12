# ____ d__ _______ d__, t.., date
# _______ __
#
# TODAY date(2018, 11, 12)
#
#
# ___ extract_dates data
#     """Extract unique dates from DB table representation as shown in Bite"""
#
#     data ?.s..
#
#
#     dates s..
#     lines ?.s..
#     ___ i,line __ e.. ?
#         __ i > 2 a.. i !_ l.. ? - 1
#             date_ __.s.. _ ^\s*\|\s(\S+)\s\| ? .g.. 1
#             year,month,day m.. i.. ?.s.. "-"
#
#             date_ d.. y.._? m.._?d.._?
#             ?.a.. ?
#
#     r.. ?

# ___ calculate_streak dates
#     """Receives sequence (set) of dates and returns number of days
#        on coding streak.
#
#        Note that a coding streak is defined as consecutive days coded
#        since yesterday, because today is not over yet, however if today
#        was coded, it counts too of course.
#
#        So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
#        the table makes for a 3 days coding streak.
#
#        See the tests for more examples that will be used to pass your code.
#     """
#     streak 0
#
#
#     delta t.. d.._1
#     day T.. - ?
#
#     w.... ? __ ?
#         ? +_ 1
#
#         ? -_ ?
#
#
#
#     __ T.. __ ?
#         ? +_ 1
#
#     r.. ?
