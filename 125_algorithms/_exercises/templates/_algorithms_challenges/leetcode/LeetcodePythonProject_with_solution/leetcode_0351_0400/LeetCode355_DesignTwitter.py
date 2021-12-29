'''
Created on Feb 28, 2018

@author: tongq
'''
class TweetObj(object):
    ___ __init__(self, tweet_id, user_id, tweetId, prevTweet_ N..
        self.user_id = user_id
        self.tweetContext = tweetId
        self.prevTweet = prevTweet
        self.tweet_id = tweet_id

class Twitter(object):

    ___ __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = {}
        self.latestTweets = {}
        self.tweet_id = 0

    ___ postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        __ userId n.. __ self.following:
            self.following[userId] = set([userId])
        self.tweet_id += 1
        __ userId __ self.latestTweets:
            prevTweet = self.latestTweets[userId]
            tweet = TweetObj(self.tweet_id, userId, tweetId, prevTweet)
            self.latestTweets[userId] = tweet
        ____:
            tweet = TweetObj(self.tweet_id, userId, tweetId, N..)
            self.latestTweets[userId] = tweet

    ___ getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        _______ heapq
        heap    # list
        __ userId n.. __ self.following:
            r.. []
        followingUsers = self.following[userId]
        followingUsers.add(userId)
        ___ following_id __ followingUsers:
            __ following_id __ self.latestTweets:
                latestTweet = self.latestTweets[following_id]
                tweetTuple = (-latestTweet.tweet_id, latestTweet.tweetContext, latestTweet.prevTweet)
                heapq.heappush(heap, tweetTuple)
        result    # list
        ___ _ __ r..(10):
            __ n.. heap:
                break
            tweetTuple = heapq.heappop(heap)
            result.a..(tweetTuple[1])
            __ tweetTuple[2]:
                newTweet = tweetTuple[2]
                newTweetTuple = (-newTweet.tweet_id, newTweet.tweetContext, newTweet.prevTweet)
                heapq.heappush(heap, newTweetTuple)
        r.. result

    ___ follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        __ followerId __ self.following:
            self.following[followerId].add(followeeId)
        ____:
            self.following[followerId] = set([followeeId])

    ___ unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        __ followerId __ self.following a.. followerId != followeeId:
            self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)