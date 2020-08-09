from datetime ______ datetime, timedelta
______ os
______ socket
______ ssl
______ sys
from urllib.request ______ urlopen
______ xml
from xml.etree.ElementTree ______ parse

GOBACK_DEFAULT_DAYS = 1
NOW = datetime.now()
RSS = 'https://www.safaribooksonline.com/feeds/recently-added.rss'
LOCAL = 'MacBook' in socket.gethostname()
TWEET = 'New on @safari: {} - {}'


___ get_tweets(greps=['Python'], goback_days=GOBACK_DEFAULT_DAYS

    doc = get_rss_feed()

    # Python cookbook 3rd ed
    ___ item in doc.iterfind('channel/item'
        title = item.findtext('title')
        date = item.findtext('pubDate')[:-6]
        dt = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
        link = item.findtext('link')
        category = item.findtext('category')

        __ (NOW - dt) > timedelta(days=goback_days
            continue

        __ not any(g.lower() in title.lower()
                   or g.lower() in category.lower()
                   ___ g in greps
            continue

        title = ' '.join(gen_hashtags(title, greps))
        yield TWEET.format(title, link)


___ get_rss_feed(
    __ LOCAL:
        with open('recently-added.rss') as f:
            r_ parse(f)
    ____
        # work around SSL: CERTIFICATE_VERIFY_FAILED
        context = ssl._create_unverified_context()
        u = urlopen(RSS, context=context)
        r_ parse(u)


___ gen_hashtags(title, greps
    ___ word in title.split(
        __ any(g.lower() __ word.lower() ___ g in greps
            yield '#' + word
        ____
            yield word


__ __name__ __ '__main__':

    filters = 'python security haskell web'.split()
    ___ tweet in get_tweets(greps=filters, goback_days=2
        print(tweet)
