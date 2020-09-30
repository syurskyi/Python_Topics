______ unittest
from unittest.mock ______ patch

______ tweepy

from whotweeted ______ get_country_code, who_is_output
from whotweeted ______ load_cache

DATA = dict(AU='875639674244444160',
            ES='875669971954806784',
            nopb='846302762736504833',
            noloc='844092059988508673',
            badid='8756396742444441da'
            )
get_tweet = lambda x: load_cache(DATA.get(x))  # noqa E731


class WhoTweetedTestCase(unittest.TestCase

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('AU'))
    ___ test_julian(self, mock_method
        tweetid = DATA.get('AU')
        country = get_country_code(tweetid)
        who_is_out = who_is_output(country)
        self.assertEqual(country, 'AU')
        self.assertIn('Julian', who_is_out)

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('ES'))
    ___ test_bob(self, mock_method
        tweetid = DATA.get('ES')
        country = get_country_code(tweetid)
        who_is_out = who_is_output(country)
        self.assertEqual(country, 'ES')
        self.assertIn('Bob', who_is_out)

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('nopb'))
    ___ test_no_pybites_account(self, mock_method
        tweetid = DATA.get('nopb')
        with self.assertRaises(ValueError
            get_country_code(tweetid)

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('noloc'))
    ___ test_no_location_in_tweet(self, mock_method
        tweetid = DATA.get('noloc')
        with self.assertRaises(AttributeError
            get_country_code(tweetid)

    # not really a return value, it crashes before decorator can cash tweet
    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('nopb'))
    ___ test_bad_tweet_id(self, mock_method
        tweetid = DATA.get('badid')
        print(tweetid)
        with self.assertRaises(ValueError
            get_country_code(tweetid)


__  -n __ '__main__':
    unittest.main()
