_______ h__


c_ Twitter(o..

  ___ -
    """
    Initialize your data structure here.
    """
    ts 0
    tweets c...d.. l..
    friendship c...d..(s..)

  ___ postTweet  userId, tweetId
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: void
    """
    tInfo ts, tweetId, userId, l..(tweets[userId])
    tweets[userId].a..(tInfo)
    ts -_ 1

  ___ getNewsFeed  userId
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    ret    # list
    heap    # list
    __ tweets[userId]:
      h__.heappush(heap, tweets[userId][-1])

    ___ followeeId __ friendship[userId]:
      __ tweets[followeeId]:
        h__.heappush(heap, tweets[followeeId][-1])
    cnt 10
    w.... heap a.. cnt > 0:
      _, tid, uid, idx h__.heappop(heap)
      ret.a..(tid)
      __ idx > 0:
        h__.heappush(heap, tweets[uid][idx - 1])
      cnt -_ 1
    r.. ret

  ___ follow  followerId, followeeId
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    __ followerId __ followeeId:
      r..
    friendship[followerId] |= {followeeId}

  ___ unfollow  followerId, followeeId
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    friendship[followerId] -_ {followeeId}

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
