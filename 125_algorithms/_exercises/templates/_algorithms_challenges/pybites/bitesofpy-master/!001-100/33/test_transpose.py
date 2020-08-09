from random ______ randint
from collections ______ namedtuple

from transpose ______ transpose

POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
         '2017-11': 12, '2017-12': 11, '2018-1': 3}
NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']

Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')


___ _gen_community(
    for name in NAMES:
        yield Member(name=name,
                     since_days=randint(1, 365),
                     karma_points=randint(1, 100),
                     bitecoin_earned=randint(1, 100))


___ test_transpose_dict(
    months, num_posts = transpose(POSTS)
    assert list(months) __ ['2017-8', '2017-9', '2017-10',
                            '2017-11', '2017-12', '2018-1']
    assert list(num_posts) __ [19, 13, 13, 12, 11, 3]


___ test_transpose_list_tuplies(
    community = list(_gen_community())
    names, days, karma, bitecoin = transpose(community)
    assert list(names) __ NAMES
    assert list(days) __ [m.since_days for m in community]
    assert list(karma) __ [m.karma_points for m in community]
    assert list(bitecoin) __ [m.bitecoin_earned for m in community]