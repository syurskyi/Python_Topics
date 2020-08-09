'''
Who am I talking to PyBites?!
Fair question: https://twitter.com/anthonypjshaw/status/875275923930480641
'''

from functools ______ wraps
______ os
______ pickle
______ re
______ sys

______ tweepy

DATA = 'data'
KNOWN_PLACES = dict(AU='Julian', ES='Bob')
PYBITES = 'pybites'
COLLECT_TEST_DATA = False
TWITTER_KEY = os.environ.get('PYB_100D_TW_KEY')
TWITTER_SECRET = os.environ.get('PYB_100D_TW_SECRET')
__ not TWITTER_KEY or not TWITTER_SECRET:
    print('Please set PYB_100D_TW_KEY and PYB_100D_TW_SECRET env vars')
    sys.exit(1)

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)


___ cache(f
    @wraps(f)
    ___ wrapped(*args, **kwargs
        tweetid = args[0]
        cache = os.path.join(DATA, tweetid)
        r = f(*args, **kwargs)
        __ COLLECT_TEST_DATA:
            pickle.dump(r, open(cache, "wb"))
        r_ r
    r_ wrapped


___ load_cache(tweetid
    cache = os.path.join(DATA, tweetid)
    r_ pickle.load(open(cache, "rb"))


@cache
___ get_status(tweetid
    r_ api.get_status(tweetid)


___ get_country_code(tweetid
    try:
        tweet = get_status(tweetid)
    # this could be various issues so print the exception string
    except tweepy.error.TweepError as exc:
        raise ValueError('Problem getting tweet:\n{}'.format(exc))

    __ tweet.user.screen_name != PYBITES:
        raise ValueError('Not a {} tweet'.format(PYBITES))

    try:
        r_ tweet.place.country_code
    except AttributeError:
        raise


___ who_is_output(country
    __ not country:
        r_ 'Unable to identify country code'

    __ country not in KNOWN_PLACES:
        r_ 'WTF?! Tweet was tweeted from {}'.format(country)

    r_ '{} tweeted it out'.format(KNOWN_PLACES[country])


__ __name__ __ '__main__':
    __ le.(sys.argv) < 2:
        sys.exit('Provide tweet id or link')

    tweetid = re.sub(r'.*status/(\d+).*', r'\1', sys.argv[1])

    try:
        country_code = get_country_code(tweetid)
    except ValueError as exc:
        print(exc)
    except AttributeError as exc:
        print('Location not set on tweet')
    ____
        output = who_is_output(country_code)
        print(output)
