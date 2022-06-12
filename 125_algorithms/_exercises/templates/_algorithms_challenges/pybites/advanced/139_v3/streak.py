# _______ __
# ____ d__ _______ d__, t.., date
#
# ONE_DAY t.. d.._1
#
# TODAY date(2018, 11, 12)
#
#
# ___ extract_dates data
#     """Extract unique dates from DB table representation as shown in Bite"""
#     dates __.f.. _  (\d{4}-\d\d-\d\d)  ?
#     r.. s.. d__.s.. d _Y-_m-_d .d.. ___ ? __ ?
#
#
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
#     dy T.. - O..
#     count 0
#     w.... ? __ ?
#         ? -_ O..
#         ? +_ 1
#     r.. ? + (1 __ T.. __ ? ____ 0
