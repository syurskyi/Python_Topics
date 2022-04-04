____ r__ _______ r..
____ c.. _______ n..

____ transpose _______ transpose

POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
         '2017-11': 12, '2017-12': 11, '2018-1': 3}
NAMES =  'Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard'

Member = n..('Member', 'name since_days karma_points bitecoin_earned')


___ _gen_community
    ___ name __ NAMES:
        y.. Member(name=name,
                     since_days=r..(1, 365),
                     karma_points=r..(1, 100),
                     bitecoin_earned=r..(1, 100


___ test_transpose_dict
    months, num_posts = transpose(POSTS)
    ... l..(months) __  '2017-8', '2017-9', '2017-10',
                            '2017-11', '2017-12', '2018-1'
    ... l..(num_posts) __ [19, 13, 13, 12, 11, 3]


___ test_transpose_list_tuplies
    community = l..(_gen_community
    names, days, karma, bitecoin = transpose(community)
    ... l..(names) __ NAMES
    ... l..(days) __ [m.since_days ___ m __ community]
    ... l..(karma) __ [m.karma_points ___ m __ community]
    ... l..(bitecoin) __ [m.bitecoin_earned ___ m __ community]