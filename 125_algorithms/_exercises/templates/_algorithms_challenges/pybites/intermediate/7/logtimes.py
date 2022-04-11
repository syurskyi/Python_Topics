# ____ d__ _______ d__, t..
# _______ __
# _______ t__
# _______ u__.r..
#
# SHUTDOWN_EVENT = 'Shutdown initiated'
#
# # prep: read in the logfile
# tmp  __.g.. TMP  /tmp
# logfile  __.p...j.. ? log
# u__.r...u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
#     ?
#
#
# w__ o..  ? __ f
#     loglines  f.r..
#
#
# # for you to code:
#
# ___ convert_to_datetime line
#     """TODO 1:
#        Extract timestamp from logline and convert it to a datetime object.
#        For example calling the function with:
#        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
#        returns:
#        datetime(2014, 7, 3, 23, 27, 51)
#     """
#     line_split  ?.s.. " "
#     ___ word __ ?
#         ___
#             line_ts  d__.s.. ? _Y-_m-_dT_H|_M|_S
#             r.. ?
#         ______
#             _____
#
#     r.. N..
#
#
# ___ time_between_shutdowns loglines
#     """TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and
#        calculate the timedelta between the first and last one.
#        Return this datetime.timedelta object.
#     """
#     shutdown_events  line.s.. "\n" ___ ? __ l __ "Shutdown initiated" __ ?
#     first_shutdown  ? ? 0
#     last_shutdown  ? ? a
#     r.. ? - ?
#
#
# #if __name__ == "__main__":
#     #print(convert_to_datetime('INFO 2014-07-03T23:27:51 supybot Shutdown initiated.\n'))
#     #print(time_between_shutdowns(loglines))