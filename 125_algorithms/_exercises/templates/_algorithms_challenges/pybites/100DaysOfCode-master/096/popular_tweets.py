from collections ______ namedtuple
______ os
______ sys
______ time

______ tweepy

from tweets ______ parse_csv

CACHE = 'cache.shelve'
FMT = '{rt:<5} | {fav:<5} | {text} ({status})'
HASHTAG_100DAYS = '#100DaysOfCode'

TWITTER_KEY = os.environ.get('PYB_100D_TW_KEY')
TWITTER_SECRET = os.environ.get('PYB_100D_TW_SECRET')
__ not TWITTER_KEY or not TWITTER_SECRET:
    print('Please set PYB_100D_TW_KEY and PYB_100D_TW_SECRET env vars')
    sys.exit(1)

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

Tweet = namedtuple('Tweet', 'status text rt fav')

tweet_stats = {}
scores = {}

___ row in parse_csv(
    status = row['tweet_id']
    tweet = row['text']
    __ tweet.startswith(HASHTAG_100DAYS
        info = api.get_status(status)
        rt, fav = info.retweet_count, info.favorite_count
        scores[status] = rt + fav
        tweet_stats[status] = Tweet(status=status,
                                    text=tweet,
                                    rt=rt,
                                    fav=fav)
        time.sleep(1)

print(FMT.format(rt='# RT', fav='# Fav', text='Tweet text', status='status'))
print('-' * 140)

___ status, score in sorted(scores.items(),
                            key=lambda kv: kv[1],
                            reverse=True
    info = tweet_stats[status]
    print(FMT.format(rt=info.rt,
                     fav=info.fav,
                     text=info.text,
                     status=info.status))
