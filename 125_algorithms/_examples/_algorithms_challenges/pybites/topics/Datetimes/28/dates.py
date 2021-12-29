import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    # Sun, 07 Jan 2018 12:00:00 +0100
    date_fmt = '%a, %d %b %Y %H:%M:%S'
    dt = datetime.strptime(date_str[:-6], date_fmt)
    return dt


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    new_list = [logdate.strftime("%Y-%m") for logdate in dates]
    return collections.Counter(new_list).most_common(1)[0][0]

converted_dates = [convert_to_datetime(d) for d in _get_dates()]
print(converted_dates[:3])
print(get_month_most_posts(converted_dates))