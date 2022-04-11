# ____ d__ _______ d__
# _______ __
# _______ u__.r..
#
# SHUTDOWN_EVENT  'Shutdown initiated'
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
# ___ convert_to_datetime line
#     """
#     Extract timestamp from logline and convert it to a datetime object.
#     For example calling the function with:
#     INFO 2014-07-03T23:27:51 supybot Shutdown complete.
#     returns: datetime(2014, 7, 3, 23, 27, 51)
#     """
#     d  ?.s.. 1
#     r.. d__.s.. ? _Y-_m-_dT_H:_M:_S
#
#
# ___ time_between_shutdowns loglines
#     """
#     Extract shutdown events ("Shutdown initiated") from loglines and
#     calculate the timedelta between the first and last one.
#     Return this datetime.timedelta object.
#     """
#     lines  l ___ ? __ ? __ ?. -c ?
#     start_date  ? ? 0
#     end_date  ? ? -1
#     r.. ? - ?