____ stay_positive _______ (tweets, filter_tweets_on_polarity,
                           order_tweets_by_polarity)


___ test_filter_tweets_keep_positive
    a.. = filter_tweets_on_polarity(tweets)
    e.. = tweets[1:4]
    ... a.. __ e..


___ test_filter_tweets_keep_negative
    a.. = filter_tweets_on_polarity(tweets, keep_positive=F..)
    e.. = [tweets[0], tweets[-1]]
    ... a.. __ e..


___ test_order_tweets_positive_highest
    a.. = [tweet.polarity ___ tweet __ order_tweets_by_polarity(tweets)]
    e.. = [1.0, 0.8, 0.125, -0.19999999999999998,
                -0.3333333333333333]
    ... a.. __ e..


___ test_order_tweets_negative_highest
    a.. = [tweet.polarity ___ tweet __
              order_tweets_by_polarity(tweets, positive_highest=F..)]
    e.. = [-0.3333333333333333, -0.19999999999999998,
                0.125, 0.8, 1.0]
    ... a.. __ e..