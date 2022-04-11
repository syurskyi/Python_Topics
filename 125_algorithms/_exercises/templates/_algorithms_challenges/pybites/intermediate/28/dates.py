_______ c..
____ d__ _______ d__
_______ __
_______ __
____ u__.r.. _______ u..

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = __.c..(r'<pubDate>(.*?)</pubDate>')
TMP = __.g.. TMP  /tmp


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
    tz = date_str.rfind("+")
    r.. d__.s..(date_str[:tz -1], "%a, %d %b %Y %H:%M:%S")


___ get_month_most_posts(dates
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    posts_yr_mo = [post_date.s..("%Y-%m") ___ post_date __ dates]
    posts_frequency = c...C..(posts_yr_mo)
    r.. posts_frequency.m..[0][0]
    

#if __name__ == "__main__":
    #print(convert_to_datetime('Thu, 04 May 2017 20:46:00 +0200'))
    #get_month_most_posts(_get_dates())