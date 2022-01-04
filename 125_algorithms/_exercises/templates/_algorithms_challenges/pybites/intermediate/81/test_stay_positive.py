____ stay_positive _______ (tweets, filter_tweets_on_polarity,
                           order_tweets_by_polarity)


___ test_filter_tweets_keep_positive
    actual = filter_tweets_on_polarity(tweets)
    expected = tweets[1:4]
    ... actual __ expected


___ test_filter_tweets_keep_negative
    actual = filter_tweets_on_polarity(tweets, keep_positive=F..)
    expected = [tweets[0], tweets[-1]]
    ... actual __ expected


___ test_order_tweets_positive_highest
    actual = [tweet.polarity ___ tweet __ order_tweets_by_polarity(tweets)]
    expected = [1.0, 0.8, 0.125, -0.19999999999999998,
                -0.3333333333333333]
    ... actual __ expected


___ test_order_tweets_negative_highest
    actual = [tweet.polarity ___ tweet __
              order_tweets_by_polarity(tweets, positive_highest=F..)]
    expected = [-0.3333333333333333, -0.19999999999999998,
                0.125, 0.8, 1.0]
    ... actual __ expected