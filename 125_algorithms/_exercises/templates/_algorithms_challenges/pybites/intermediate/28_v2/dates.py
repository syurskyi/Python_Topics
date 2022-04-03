_______ c..
____ d__ _______ d__
_______ __
_______ __
____ u__.r.. _______ u..

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = __.c..(r'<pubDate>(.*?)</pubDate>')
TMP = __.getenv("TMP", "/tmp")


___ _get_dates
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = __.p...j..(BASE_URL, RSS_FEED)
    local = __.p...j..(TMP, RSS_FEED)
    u..(remote, local)

    w__ o.. local) __ f:
        r.. PUB_DATE.f..(f.read


___ convert_to_datetime(date_str
    """Receives a date str and convert it into a datetime object"""

    r.. d__.s..(date_str,'%a, %d %b %Y %H:%M:%S %z')



___ get_month_most_posts(dates
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""

    counts = c...Counter(date.s..("%Y-%m") ___ date __ dates)

    r.. counts.most_common(1)[0][0]


