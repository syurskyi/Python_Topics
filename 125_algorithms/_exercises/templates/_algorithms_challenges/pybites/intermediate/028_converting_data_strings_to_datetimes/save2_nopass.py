____ collections _______ Counter
____ d__ _______ d__
_______ os
_______ __
____ urllib.request _______ urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = __.c..(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


___ _get_dates
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.j..(BASE_URL, RSS_FEED)
    local = os.path.j..(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) __ f:
        r.. PUB_DATE.f..(f.read())


___ convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    date_str = ' '.j..(date_str.s.. [1:5])[:-3]
    r.. d__.strptime(date_str, '%d %b %Y %H:%M')


___ get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    y = [convert_to_datetime(d).year ___ d __ dates]
    m = [convert_to_datetime(d).month ___ d __ dates]
    l = l..(z..(y, m))
    most_freq_month = s..(Counter(l).most_common()[0][0])
    output = d__.strptime(most_freq_month, '(%Y, %m)')
    r.. output.strftime('%Y-%m')