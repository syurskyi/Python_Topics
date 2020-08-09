______ collections
from datetime ______ datetime
______ os
______ re
from urllib.request ______ urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


___ _get_dates(
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        r_ PUB_DATE.findall(f.read())


___ convert_to_datetime(date_str
    """Receives a date str and convert it into a datetime object"""
    r_ datetime.strptime(date_str.split('+')[0].strip(), '%a, %d %b %Y %H:%M:%S')


___ get_month_most_posts(dates
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    months = collections.defaultdict(int)
    ___ x in dates:
        months[f'{x.year:04}-{x.month:02}'] += 1
    r_ sorted(months.items(), key=lambda k_v: -k_v[1])[0][0]
