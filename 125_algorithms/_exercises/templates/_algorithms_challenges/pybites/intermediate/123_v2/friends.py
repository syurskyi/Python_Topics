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
    friend_counts d..(l..)
    

    most_friends f__("-inf")


    ___ friend_1,friend_2 __ friendships:
        friend_counts[friend_1].a..(users[friend_2])
        friend_counts[friend_2].a..(users[friend_1])



    top_user m..(friend_counts,key=l.... x: l..(friend_counts[x]

    r.. users[top_user],friend_counts[top_user]
