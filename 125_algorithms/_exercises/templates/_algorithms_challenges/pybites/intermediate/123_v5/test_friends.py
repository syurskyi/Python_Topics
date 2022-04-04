____ friends _______ get_friend_with_most_friends, friendships


___ test_default_friendships_list
    user, friends = get_friend_with_most_friends(friendships)
    ... user __ 'sara'
    ... s..(l..(friends __  'joyce', 'kevin', 'nick', 'rod'


___ test_different_friendships_list
    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    user, friends = get_friend_with_most_friends(friendships)
    ... user __ 'joyce'
    ... s..(l..(friends __  'beverly', 'julian', 'kevin', 'nick',
                                     'rod', 'sara'


___ test_friendships_list_with_duplicate_names
    names = 'bob bob tim tim julian julian'.s.. 
    ids = r..(l..(names
    users = d..(z..(ids, names

    friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3),
                   (2, 4), (4, 5)]
    user, friends = get_friend_with_most_friends(friendships, users=users)
    ... user __ 'bob'
    ... s..(l..(friends __  'bob', 'julian', 'julian', 'tim'