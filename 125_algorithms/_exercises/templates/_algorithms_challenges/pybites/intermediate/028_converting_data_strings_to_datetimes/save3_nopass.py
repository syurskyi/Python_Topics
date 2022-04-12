# ____ c.. _______ C..
# ____ d__ _______ d__
# _______ __
# _______ __
# ____ u__.r.. _______ u..
#
# BASE_URL 'https://bites-data.s3.us-east-2.amazonaws.com/'
# RSS_FEED 'pybites_feed.rss.xml'
# PUB_DATE __.c.. _ <pubDate>(.*?)</pubDate>
# TMP '/tmp'
#
#
# ___ _get_dates
#     """Downloads PyBites feed and parses out all pub dates returning
#        a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
#        'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
#     remote __.p...j.. B.. R..
#     local __.p...j.. T.. R..
#     u.. ? ?
#
#     w__ o.. l.. __ f
#         r.. P__.f.. ?.r..
#
#
# ___ convert_to_datetime date_str
#     """Receives a date str and convert it into a datetime object"""
#     date_str s.. ?
#     date_str ' '.j.. ?.s..  1|5 |-3
#     r.. d__.s.. ? _d _b _Y _H|_M
#
#
# ___ get_month_most_posts dates
#     """Receives a list of datetimes and returns the month (format YYYY-MM)
#        that occurs most"""
#     y  ? d .y.. ___ ? __ ?
#     m  ? d .m.. ___ ? __ ?
#     l l.. z.. ? ?
#     most_freq_month s.. C.. ? .m.. 1 0 0
#     output d__.s.. ? _Y, _m
#     r.. ?.s.. _Y-_m