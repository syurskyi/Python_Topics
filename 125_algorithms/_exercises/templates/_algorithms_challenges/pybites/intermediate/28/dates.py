_______ collections
____ d__ _______ d__
_______ os
_______ re
____ urllib.request _______ urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")


___ _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        r.. PUB_DATE.findall(f.read())


___ convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    tz = date_str.rfind("+")
    r.. d__.strptime(date_str[:tz -1], "%a, %d %b %Y %H:%M:%S")


___ get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    posts_yr_mo = [post_date.strftime("%Y-%m") ___ post_date __ dates]
    posts_frequency = collections.Counter(posts_yr_mo)
    r.. posts_frequency.most_common()[0][0]
    

#if __name__ == "__main__":
    #print(convert_to_datetime('Thu, 04 May 2017 20:46:00 +0200'))
    #get_month_most_posts(_get_dates())