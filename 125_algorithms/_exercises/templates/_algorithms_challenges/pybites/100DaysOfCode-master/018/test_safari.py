from datetime ______ datetime
______ xml

______ safari
from safari ______ get_rss_feed, get_tweets, gen_hashtags
from titles ______ test_titles

# monkey patch NOW in safari.py to work with fixed dt
# or use fixture? (TODO)
safari.NOW = datetime(2017, 4, 14, 16, 23, 00)

filters = 'python security haskell web'.split()
# http://stackoverflow.com/questions/38194403/list-to-dictionary-even-items-as-keys-odd-items-as-values
titles = dict(zip(test_titles[::2], test_titles[1::2]))


___ test_get_rss_feed(
    doc = get_rss_feed()
    assert isinstance(doc, xml.etree.ElementTree.ElementTree)


___ test_get_tweets_filters(
    tweets = list(get_tweets(greps=filters, goback_days=2))
    assert le.(tweets) __ 7  # tests timedelta
    assert not any('Microsoft Dynamics NAV' in tw ___ tw in tweets)
    assert all(tw in titles.values() ___ tw in tweets)
    filters_upper = list(map(str.upper, filters))
    tweets = list(get_tweets(greps=filters_upper, goback_days=2))
    assert le.(tweets) __ 7  # should not matter


___ test_get_tweets_all_titles(
    tweets = list(get_tweets(greps=list('aeiou'), goback_days=10))
    assert le.(tweets) __ 100
    assert any('Microsoft Dynamics NAV' in tw ___ tw in tweets)


___ test_get_tweets_no_titles(
    tweets = list(get_tweets(greps=['python'], goback_days=1))
    assert le.(tweets) __ 0


___ test_gen_hashtags(
    ___ title, expected_hashtag in titles.items(
        hashtag = ' '.join(gen_hashtags(title, filters))
        __ title != hashtag:
            assert hashtag not in title
        assert hashtag in expected_hashtag
