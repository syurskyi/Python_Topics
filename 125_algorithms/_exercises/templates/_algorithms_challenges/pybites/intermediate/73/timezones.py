# _______ pytz
# ____ d__ _______ d__
#
# MEETING_HOURS  r..(6, 23)  # meet from 6 - 22 max
# TIMEZONES  s.. p__.a..
#
#
# ___ within_schedule utc $timezones
#    """Receive a utc datetime and one or more timezones and check if
#       they are all within schedule (MEETING_HOURS)"""
#
#    ___ time_z __ ?
#
#       __ time_z n.. __ T..
#          r.. V... "Please use valid timezone"
#
#       new_tz  p__.t.. ?
#
#       utc_localized  new_tz.l.. u..
#       utc_localized_offset  i.. ? .u__ .t../60/60
#       time_difference  utc.h.. + ?
#
#       __ t.. n.. __ M..
#          r.. F..
#    r.. T..