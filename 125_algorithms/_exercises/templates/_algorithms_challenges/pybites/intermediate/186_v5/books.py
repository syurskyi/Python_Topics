# ____ d__ _______ d__
#
# ____ d__.p.. _______ p..
#
# # work with a static date for tests, real use = datetime.now()
# NOW d__(2019, 3, 17, 16, 28, 42, 966663)
# WEEKS_PER_YEAR 52
# START_DATE d__(2018, 12, 24)
#
#
# ___ get_number_books_read books_per_year_goal i..
#                           at_date s.. N.. __ i..
#     """Based on books_per_year_goal and at_date, return the
#        number of books that should have been read.
#        If books_per_year_goal negative or 0, or at_date is in the
#        past, raise a ValueError."""
#     at_date ? o. s.. N..
#     target p.. ?
#
#     __ ? < S.. o. b.. < 1
#         r.. V...
#
#     week_diff t__.d.. - S__.d__.d.. // 7
#
#     r.. i.. ? / W.. * b..
