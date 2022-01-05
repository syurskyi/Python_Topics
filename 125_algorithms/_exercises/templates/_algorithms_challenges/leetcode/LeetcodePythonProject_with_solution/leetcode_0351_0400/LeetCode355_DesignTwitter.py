'''
Created on Feb 28, 2018

@author: tongq
'''
c_ TweetObj(o..):
    ___ - , tweet_id, user_id, tweetId, prevTweet_ N..
        user_id = user_id
        tweetContext = tweetId
        prevTweet = prevTweet
        tweet_id = tweet_id

c_ Twitter(o..):

    ___ - ):
        """
        Initialize your data structure here.
        """
        following    # dict
        latestTweets    # dict
        tweet_id = 0

    ___ postTweet  userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        __ userId n.. __ following:
            following[userId] = set([userId])
        tweet_id += 1
        __ userId __ latestTweets:
            prevTweet = latestTweets[userId]
            tweet = TweetObj(tweet_id, userId, tweetId, prevTweet)
            latestTweets[userId] = tweet
        ____:
            tweet = TweetObj(tweet_id, userId, tweetId, N..)
            latestTweets[userId] = tweet

    ___ getNewsFeed  userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        _______ heapq
        heap    # list
        __ userId n.. __ following:
            r.. []
        followingUsers = following[userId]
        followingUsers.add(userId)
        ___ following_id __ followingUsers:
            __ following_id __ latestTweets:
                latestTweet = latestTweets[following_id]
                tweetTuple = (-latestTweet.tweet_id, latestTweet.tweetContext, latestTweet.prevTweet)
                heapq.heappush(heap, tweetTuple)
        result    # list
        ___ _ __ r..(10):
            __ n.. heap:
                _____
            tweetTuple = heapq.heappop(heap)
            result.a..(tweetTuple[1])
            __ tweetTuple[2]:
                newTweet = tweetTuple[2]
                newTweetTuple = (-newTweet.tweet_id, newTweet.tweetContext, newTweet.prevTweet)
                heapq.heappush(heap, newTweetTuple)
        r.. result

    ___ follow  followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        __ followerId __ following:
            following[followerId].add(followeeId)
        ____:
            following[followerId] = set([followeeId])

    ___ unfollow  followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        __ followerId __ following a.. followerId != followeeId:
            following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)