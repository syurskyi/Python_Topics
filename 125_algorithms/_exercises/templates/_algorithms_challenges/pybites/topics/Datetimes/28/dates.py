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
    # Sun, 07 Jan 2018 12:00:00 +0100
    date_fmt = '%a, %d %b %Y %H:%M:%S'
    dt = d__.s..(date_str[:-6], date_fmt)
    r.. dt


___ get_month_most_posts(dates
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    new_list = [logdate.s..("%Y-%m") ___ logdate __ dates]
    r.. c...C..(new_list).most_common(1)[0][0]

converted_dates = [convert_to_datetime(d) ___ d __ _get_dates()]
print(converted_dates[:3])
print(get_month_most_posts(converted_dates))