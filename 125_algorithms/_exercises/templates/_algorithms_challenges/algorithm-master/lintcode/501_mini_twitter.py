"""
Definition of Tweet:
class Tweet:
    @classmethod
    ___ create(cls, user_id, tweet_text
         # This will create a new tweet object,
         # and auto fill id
"""


class MiniTwitter:
    ___ __init__(self
        self.timestamp = 0
        self.tweets = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    ___ postTweet(self, user_id, tweet_text
        __ user_id not in self.tweets:
            self.tweets[user_id] = []

        self.timestamp += 1
        self.tweets[user_id].append((
            self.timestamp,
            Tweet.create(user_id, tweet_text),
        ))

        r_ self.tweets[user_id][-1][1]

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    ___ getNewsFeed(self, user_id
        res = []

        __ user_id in self.tweets:
            res.extend(self.tweets[user_id][-10:])

        __ user_id in self.followings:
            ___ follow_id in self.followings[user_id]:
                __ follow_id in self.tweets:
                    res.extend(self.tweets[follow_id][-10:])

        __ not res:
            r_ []

        res.sort()
        r_ [tweet ___ _, tweet in res[-10:]][::-1]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    ___ getTimeline(self, user_id
        __ user_id not in self.tweets:
            r_ []

        r_ [tweet ___ _, tweet in self.tweets[user_id][-10:]][::-1]

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ follow(self, from_id, to_id
        __ from_id not in self.followings:
            self.followings[from_id] = set()

        __ to_id in self.followings[from_id]:
            r_

        self.followings[from_id].add(to_id)

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    ___ unfollow(self, from_id, to_id
        __ from_id not in self.followings:
            r_

        __ to_id not in self.followings[from_id]:
            r_

        self.followings[from_id].discard(to_id)
