____ c.. _______ d..

names 'bob julian tim martin rod sara joyce nick beverly kevin'.s..
ids r..(l..(names
users d..(z..(ids, names  # 0: bob, 1: julian, etc

friendships [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


___ get_friend_with_most_friends(friendships, users=users
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    d d.. l..
    ___ user, friend __ friendships:
        __ friend n.. __ d[user]:
            d[user].a..(friend)
        __ user n.. __ d[friend]:
            d[friend].a..(user)

    user_with_max_friends m..(d, k.._l.... x: l..(d.g.. x)))
    r.. (users[user_with_max_friends],
            [users[x] ___ x __ d[user_with_max_friends]])
