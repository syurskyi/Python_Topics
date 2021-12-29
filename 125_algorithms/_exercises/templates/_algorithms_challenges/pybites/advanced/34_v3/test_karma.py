____ karma _______ User, Transaction

alice = User('alice')
bob = User('bob')
tim = User('tim')

transactions = [
    Transaction(giver=alice, points=1),
    Transaction(giver=bob, points=2),
    Transaction(giver=tim, points=3),
    Transaction(giver=tim, points=4),
    Transaction(giver=alice, points=2),
]


___ test_init():
    ... alice.name __ 'alice'
    ... bob.name __ 'bob'
    ... tim.name __ 'tim'
    ... alice._transactions __ []
    ... bob._transactions __ []
    ... tim._transactions __ []


___ test_adding_karma():
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


___ test_upvotes_property():
    ... bob.points __ [1, 3]
    ... alice.points __ [2, 4]
    ... tim.points __ [2]


___ test_fans_property():
    ... tim.fans __ 1
    ... bob.fans __ 2
    ... alice.fans __ 2


___ test_str_dunder():
    ... s..(tim) __ 'tim has a karma of 2 and 1 fan'
    ... s..(alice) __ 'alice has a karma of 6 and 2 fans'
    ... s..(bob) __ 'bob has a karma of 4 and 2 fans'