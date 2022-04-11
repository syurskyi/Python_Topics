_______ p__

____ karma _______ User, Transaction


?p__.f..
___ bob
    r.. ? 'bob')


?p__.f..
___ tim
    r.. ? 'tim')


?p__.f..
___ alice
    r.. ? 'alice')


?p__.f..
___ transactions(bob, tim, alice
    r.. [
        Transaction(giver=alice, points=1),
        Transaction(giver=bob, points=2),
        Transaction(giver=tim, points=3),
        Transaction(giver=tim, points=4),
        Transaction(giver=alice, points=2),
    ]


___ test_init(transactions, bob, tim, alice
    ... alice.n.. __ 'alice'
    ... bob.n.. __ 'bob'
    ... tim.n.. __ 'tim'
    ... alice._transactions __ []
    ... bob._transactions __ []
    ... tim._transactions __ []


___ test_scores_and_points(transactions, bob, tim, alice
    bob + transactions[0]
    ... bob.karma __ 1
    alice + transactions[1]
    ... alice.karma __ 2
    bob + transactions[2]
    ... bob.karma __ 4
    alice + transactions[3]
    ... alice.karma __ 6
    tim + transactions[4]
    ... tim.karma __ 2
    # point lists at this point
    ... bob.points __ [1, 3]
    ... alice.points __ [2, 4]
    ... tim.points __ [2]


___ test_fans_property(transactions, bob, tim, alice
    tim + transactions[4]
    ... tim.fans __ 1
    bob + transactions[0]
    bob + transactions[0]  # same giver, does not increase fan count
    ... bob.fans __ 1
    alice + transactions[1]
    alice + transactions[2]
    ... alice.fans __ 2


___ test_str_dunder(transactions, bob, tim, alice
    tim + transactions[4]
    ... s..(tim) __ 'tim has a karma of 2 and 1 fan'
    alice + transactions[1]
    alice + transactions[3]
    ... s..(alice) __ 'alice has a karma of 6 and 2 fans'
