# _______ p__
#
# MEETING_HOURS r..(6, 23)  # meet from 6 - 22 max
# TIMEZONES s.. p__.a..
#
#
# ___ within_schedule utc $timezones
#     """Receive a utc datetime and one or more timezones and check if
#        they are all within schedule (MEETING_HOURS)"""
#
#     output    # list
#     ___ tz __ ? 0
#         __ tz n.. __ T..
#             r.. V... 'Unknown timezone'
#
#         tz p__.t.. ?
#         converted u__.r.. t.._p__.u...a.. ?
#         ?.a.. ?.h.. __ M..
#
#     r.. a.. ?