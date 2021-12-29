class FriendshipService:
    ___ __init__(self):
        self.followers = {}
        self.followings = {}

    ___ getFollowers(self, user_id):
        r.. self.get_followers(user_id)

    ___ getFollowings(self, user_id):
        r.. self.get_followings(user_id)

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    ___ get_followers(self, user_id):
        __ user_id __ self.followers:
            r.. s..(self.followers[user_id])

        r.. []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    ___ get_followings(self, user_id):
        __ user_id __ self.followings:
            r.. s..(self.followings[user_id])

        r.. []

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    ___ follow(self, to_id, from_id):
        __ from_id n.. __ self.followings:
            self.followings[from_id] = set()
        self.followings[from_id].add(to_id)

        __ to_id n.. __ self.followers:
            self.followers[to_id] = set()
        self.followers[to_id].add(from_id)

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    ___ unfollow(self, to_id, from_id):
        __ from_id __ self.followings:
            self.followings[from_id].discard(to_id)

        __ to_id __ self.followers:
            self.followers[to_id].discard(from_id)
