# _______ j__
# ____ dateutil.tz _______ gettz
# ____ d__ _______ d__, t.., tzinfo
# ____ d__.p.. _______ p..
# ____ p.. _______ P..
# _______ r__
# ____ t___ _______ T.., O.., L..
# _______ __
#
# DATA_FILE_NAME "test1.json"
# TMP P.. __.g.. "TMP", "/tmp"
#
#
# DATA_PATH T.. / D..
# MY_TZ gettz("America/New York")
# UTC gettz("UTC")
#
#
# ___ longest_streak
#     data_file: P.. D.. my_tz: O.. t.. M..
# ) __ O.. T.. date, date
#     """Retrieve datetime strings of passed commits and calculate the longest
#     streak from the user's data
#
#     Note: The datetime strings will need to be used to create aware datetime objects
#
#     All datetimes are in UTC, and the timezone of the user is part of the context
#     for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
#     New York City. You will need to convert datetimes from UTC into the supplied timezone.
#
#     The tests show an example of how a streak can change based on the timezone used.
#
#     If the dataset has two or more streaks of the same length as longest, provide
#     only the most recent streak.
#
#     Return a tuple containing start and end date for the longest streak
#     or None
#     """
#     w__ o.. ? __ f
#         data j__.l.. ?
#     # You code from here
#     commits data 'commits'
#     longest_streak f__("-inf")
#     start_date end_date N..
#
#     day_timedelta t.. d.._1
#     previous_date= current_start =N..
#     current_streak 1
#     ___ i __ r.. l.. c..
#         commit ? ?
#         __ ? 'passed'
#             date p.. ? 'date'
#             date ?.a.. m..
#
#
#             date ?.d..
#
#
#             __ ? + d.. __ p..
#                 c.. +_ 1
#             ____
#                 __ c.. > l..
#                     l.. c..
#                     start_date c.. __ c.. ____ d..
#                     end_date p.. __ p.. ____ d..
#
#
#                 c.. 1
#                 c.. d..
#
#
#             p.. d..
#
#
#
#     __ c.. > l..
#         l.. c..
#         start_date c..
#         end_date p..
#
#
#
#     __ s..
#
#         r.. ..e s..e
#
#
# __ _______ __ _______
#     streak l..
#     print _* My longest streak went from ? 0 through ? 1
#     print _* The streak lasted ? 1 - ? 0.d.. + 1?| days
