"""
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
"""


class MiniTwitter:
    ___ __init__(self):
        self.timestamp = 0
        self.tweets = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    ___ postTweet(self, user_id, tweet_text):
        __ user_id n.. __ self.tweets:
            self.tweets[user_id]    # list

        self.timestamp += 1
        self.tweets[user_id].a..((
            self.timestamp,
            Tweet.create(user_id, tweet_text),
        ))

        r.. self.tweets[user_id][-1][1]

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    ___ getNewsFeed(self, user_id):
        res    # list

        __ user_id __ self.tweets:
            res.extend(self.tweets[user_id][-10:])

        __ user_id __ self.followings:
            ___ follow_id __ self.followings[user_id]:
                __ follow_id __ self.tweets:
                    res.extend(self.tweets[follow_id][-10:])

        __ n.. res:
            r.. []

        res.s..()
        r.. [tweet ___ _, tweet __ res[-10:]][::-1]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    ___ getTimeline(self, user_id):
        __ user_id n.. __ self.tweets:
            r.. []

        r.. [tweet ___ _, tweet __ self.tweets[user_id][-10:]][::-1]

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ follow(self, from_id, to_id):
        __ from_id n.. __ self.followings:
            self.followings[from_id] = set()

        __ to_id __ self.followings[from_id]:
            r..

        self.followings[from_id].add(to_id)

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ unfollow(self, from_id, to_id):
        __ from_id n.. __ self.followings:
            r..

        __ to_id n.. __ self.followings[from_id]:
            r..

        self.followings[from_id].discard(to_id)
