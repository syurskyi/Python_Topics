from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    d = defaultdict(list)
    for user, friend in friendships:
        if friend not in d[user]:
            d[user].append(friend)
        if user not in d[friend]:
            d[friend].append(user)

    user_with_max_friends = max(d, key=lambda x: len(d.get(x)))
    return (users[user_with_max_friends],
            [users[x] for x in d[user_with_max_friends]])
