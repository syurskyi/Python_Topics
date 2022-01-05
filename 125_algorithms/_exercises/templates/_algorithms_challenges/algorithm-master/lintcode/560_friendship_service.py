c_ FriendshipService:
    ___ - ):
        followers    # dict
        followings    # dict

    ___ getFollowers  user_id):
        r.. get_followers(user_id)

    ___ getFollowings  user_id):
        r.. get_followings(user_id)

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    ___ get_followers  user_id):
        __ user_id __ followers:
            r.. s..(followers[user_id])

        r.. []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    ___ get_followings  user_id):
        __ user_id __ followings:
            r.. s..(followings[user_id])

        r.. []

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    ___ follow  to_id, from_id):
        __ from_id n.. __ followings:
            followings[from_id] = set()
        followings[from_id].add(to_id)

        __ to_id n.. __ followers:
            followers[to_id] = set()
        followers[to_id].add(from_id)

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    ___ unfollow  to_id, from_id):
        __ from_id __ followings:
            followings[from_id].discard(to_id)

        __ to_id __ followers:
            followers[to_id].discard(from_id)
