# ____ d__ _______ d__, t..
# ____ r__ _______ s..
#
# _______ p__
#
# ____ ? _______ ?
#
#
# ___ _create_dates missing  y.._2019  m.._2
#     """Helper function to build up test cases.
#
#        Returns a list of dates omitting days given
#        in the missing argument.
#
#        You can optionally specify year and month.
#     """
#     first date y.._?  m.._?  d.._1
#     last first.r.. m.._?+1 - t.. d.._1
#
#     # always yield first and last, for the in between dates
#     # only the ones not in missing
#     y.. f..
#
#     ___ day __ r.. ?.d.. + 1 ?.d..
#         __ day n.. __ missing
#             y.. f...r.. d.._?
#
#     y.. l..
#
#
# ?p__.m__.p. "missing, month", [
#     ([2, 7, 11], 2),
#     (l..(r..(2, 12, 2, 3),
#     ([14, 12], 3),
#     ([2, 3, 7, 9], 4),
#     ([1, 3, 7, 31], 5),  # expected = 3, 7, not start/end month
#     (l..(r..(1, 31, 6),  # 0 missing
#
# ___ test_get_missing_dates missing month
#     my_date_range l.. ? missing  m.._?
#     start, end ? 0 .d.. ? -1 .d..
#
#     # order passed in arg should not matter
#     s.. ?
#
#     # get days from return sequence
#     a.. s.. d.d.. ___ d __
#                     g.. m..
#
#     # filter out begin and end dates of range
#     e.. s.. d ___ ? __ m.. __
#                       ? n.. __ s.. e..
#
#     ... a.. __ e..
