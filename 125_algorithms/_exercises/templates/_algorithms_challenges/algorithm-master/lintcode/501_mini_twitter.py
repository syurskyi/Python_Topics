"""
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
"""


c_ MiniTwitter:
    ___ -
        timestamp = 0
        tweets    # dict
        followings    # dict

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    ___ postTweet  user_id, tweet_text
        __ user_id n.. __ tweets:
            tweets[user_id]    # list

        timestamp += 1
        tweets[user_id].a..((
            timestamp,
            Tweet.create(user_id, tweet_text),
        ))

        r.. tweets[user_id][-1][1]

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    ___ getNewsFeed  user_id
        res    # list

        __ user_id __ tweets:
            res.extend(tweets[user_id][-10:])

        __ user_id __ followings:
            ___ follow_id __ followings[user_id]:
                __ follow_id __ tweets:
                    res.extend(tweets[follow_id][-10:])

        __ n.. res:
            r.. []

        res.s..()
        r.. [tweet ___ _, tweet __ res[-10:]][::-1]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    ___ getTimeline  user_id
        __ user_id n.. __ tweets:
            r.. []

        r.. [tweet ___ _, tweet __ tweets[user_id][-10:]][::-1]

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ follow  from_id, to_id
        __ from_id n.. __ followings:
            followings[from_id] = s..()

        __ to_id __ followings[from_id]:
            r..

        followings[from_id].add(to_id)

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ unfollow  from_id, to_id
        __ from_id n.. __ followings:
            r..

        __ to_id n.. __ followings[from_id]:
            r..

        followings[from_id].discard(to_id)
