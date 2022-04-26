# ____ d__ _______ date
#
# _______ p__
#
# ____ ? _______ ? ?
#
#
# ?p__.f.. s.._='module'
# ___ bd
#     """This creates a bday dict that can be shared among the tests
#        (scope = module)"""
#     r.. ?
#
#
# ___ test_2_bdays_different_dates_not_print_msg bd capfd
#     bd 'bob'   ? 1987, 6, 15
#     bd 'tim'   ? 1984, 7, 15
#     output ?.r .. 0 .s..
#     ... n.. ?.s..
#
#
# ___ test_another_bday_same_yymmdd_print_msg bd capfd
#     bd 'mary'   ? 1987, 6, 15
#     output ?.r .. 0 .s..
#     ... ? __ ?.f.. 'mary'  # exactly the same as bob
#
#
# ___ test_another_bday_same_yymm_diff_day_not_print_msg bd capfd
#     # not a bday match
#     bd 'sara'  ? 1987, 6, 14
#     output ?.r .. 0 .s..
#     ... n.. ?.s..
#
#
# ___ test_another_bday_same_mmdd_diff_year_print_msg bd capfd
#     # if same day and month, but different year = match
#     bd 'mike'  ? 1981, 7, 15  # same as tim, except year
#     output ?.r .. 0 .s..
#     ... ? __ ?.f.. 'mike'