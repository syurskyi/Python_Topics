from karma import User, Transaction

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


def test_init():
    a__ alice.name == 'alice'
    a__ bob.name == 'bob'
    a__ tim.name == 'tim'
    a__ alice._transactions == []
    a__ bob._transactions == []
    a__ tim._transactions == []


def test_adding_karma():
    bob + transactions[0]
    a__ bob.karma == 1
    alice + transactions[1]
    a__ alice.karma == 2
    bob + transactions[2]
    a__ bob.karma == 4
    alice + transactions[3]
    a__ alice.karma == 6
    tim + transactions[4]
    a__ tim.karma == 2


def test_upvotes_property():
    a__ bob.points == [1, 3]
    a__ alice.points == [2, 4]
    a__ tim.points == [2]


def test_fans_property():
    a__ tim.fans == 1
    a__ bob.fans == 2
    a__ alice.fans == 2


def test_str_dunder():
    a__ str(tim) == 'tim has a karma of 2 and 1 fan'
    a__ str(alice) == 'alice has a karma of 6 and 2 fans'
    a__ str(bob) == 'bob has a karma of 4 and 2 fans'