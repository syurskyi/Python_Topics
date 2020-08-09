from karma ______ User, Transaction

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


___ test_init(
    assert alice.name __ 'alice'
    assert bob.name __ 'bob'
    assert tim.name __ 'tim'
    assert alice._transactions __ []
    assert bob._transactions __ []
    assert tim._transactions __ []


___ test_adding_karma(
    bob + transactions[0]
    assert bob.karma __ 1
    alice + transactions[1]
    assert alice.karma __ 2
    bob + transactions[2]
    assert bob.karma __ 4
    alice + transactions[3]
    assert alice.karma __ 6
    tim + transactions[4]
    assert tim.karma __ 2


___ test_upvotes_property(
    assert bob.points __ [1, 3]
    assert alice.points __ [2, 4]
    assert tim.points __ [2]


___ test_fans_property(
    assert tim.fans __ 1
    assert bob.fans __ 2
    assert alice.fans __ 2


___ test_str_dunder(
    assert str(tim) __ 'tim has a karma of 2 and 1 fan'
    assert str(alice) __ 'alice has a karma of 6 and 2 fans'
    assert str(bob) __ 'bob has a karma of 4 and 2 fans'