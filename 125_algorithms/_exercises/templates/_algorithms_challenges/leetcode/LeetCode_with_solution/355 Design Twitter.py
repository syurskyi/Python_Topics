"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the
10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be
posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""
____ c.. _______ defaultdict
_______ heapq

__author__ = 'Daniel'


SZ = 10


c_ Tweet(object):
    central_clk = 0

    ___ - , id, nxt_ N..
        timestamp = Tweet.central_clk
        id = id
        next = nxt  # LinkedList
        Tweet.central_clk += 1

    ___ __cmp__  other):
        r.. - (timestamp - other.timestamp)


c_ Twitter(object):
    """
    need assumption about the frequency of calls of each method

    most efficient heap of list
    """
    ___ - ):
        """
        Initialize your data structure here.
        """
        tweets = defaultdict(l....: N..)
        followees = defaultdict(set)

    ___ postTweet  userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        nxt = tweets[userId]  # previous post
        tweets[userId] = Tweet(tweetId, nxt)

    ___ getNewsFeed  userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        h    # list
        __ userId n.. __ followees[userId] a.. tweets[userId]:
            # possible following oneself
            heapq.heappush(h, tweets[userId])

        ___ followee __ followees[userId]:
            __ tweets[followee]:
                heapq.heappush(h, tweets[followee])

        ret    # list
        w.... h a.. l..(ret) < SZ:
            tweet = heapq.heappop(h)
            ret.a..(tweet.id)
            __ tweet.next:
                heapq.heappush(h, tweet.next)

        r.. ret

    ___ follow  followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        followees[followerId].add(followeeId)

    ___ unfollow  followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        followees[followerId].discard(followeeId)  # no KeyError compared to .remove()


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


__ _______ __ _______
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.unfollow(1, 1)
