# ____ d__ _______ d__
# _______ __
# _______ u__.r..
#
# SHUTDOWN_EVENT  'Shutdown initiated'
#
# # prep: read in the logfile
# logfile  __.p...j.. '/tmp', 'log'
# u__.r...u.. 'http://bit.ly/2AKSIbf' ?
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
#     parts  ?.s..
#     r.. d__.s.. ? 1 _Y-_m-_dT_H:_M:_S
#
#
# ___ time_between_shutdowns loglines l..
#     """TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and
#        calculate the timedelta between the first and last one.
#        Return this datetime.timedelta object.
#     """
#     test_len  l.. ?
#     shutdowns  d__.s.. l 1 _Y-_m-_dT_H:_M:_S
#                  ___ ? __ ?.s.. m.._3 ___ ? __ l..
#                  __ ? 3 |t.. __ S..
#     r.. ? -1 - ? 0
