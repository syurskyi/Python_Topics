# _______ c..
# ____ d__ _______ d__
# _______ __
# _______ __
# ____ u__.r.. _______ u..
#
# BASE_URL 'https://bites-data.s3.us-east-2.amazonaws.com/'
# RSS_FEED 'pybites_feed.rss.xml'
# PUB_DATE __.c..(r'<pubDate>(.*?)</pubDate>')
# TMP __.g.. TMP  /tmp
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
#     tz ?.r.. "+"
#     r.. d__.s.. ? |? -1 _a, _d _b _Y _H:_M:_S
#
#
# ___ get_month_most_posts dates
#     """Receives a list of datetimes and returns the month (format YYYY-MM)
#        that occurs most"""
#     posts_yr_mo  post_date.s.. _Y-_m  ___ ? __ ?
#     posts_frequency c...C.. ?
#     r.. ?.m.. 0 0
#
#
# #if __name__ == "__main__":
#     #print(convert_to_datetime('Thu, 04 May 2017 20:46:00 +0200'))
#     #get_month_most_posts(_get_dates())