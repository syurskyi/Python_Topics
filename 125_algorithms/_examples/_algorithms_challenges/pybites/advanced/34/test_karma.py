import pytest

from karma import User, Transaction


@pytest.fixture
def bob():
    return User('bob')


@pytest.fixture
def tim():
    return User('tim')


@pytest.fixture
def alice():
    return User('alice')


@pytest.fixture
def transactions(bob, tim, alice):
    return [
        Transaction(giver=alice, points=1),
        Transaction(giver=bob, points=2),
        Transaction(giver=tim, points=3),
        Transaction(giver=tim, points=4),
        Transaction(giver=alice, points=2),
    ]


def test_init(transactions, bob, tim, alice):
    assert alice.name == 'alice'
    assert bob.name == 'bob'
    assert tim.name == 'tim'
    assert alice._transactions == []
    assert bob._transactions == []
    assert tim._transactions == []


def test_scores_and_points(transactions, bob, tim, alice):
    bob + transactions[0]
    assert bob.karma == 1
    alice + transactions[1]
    assert alice.karma == 2
    bob + transactions[2]
    assert bob.karma == 4
    alice + transactions[3]
    assert alice.karma == 6
    tim + transactions[4]
    assert tim.karma == 2
    # point lists at this point
    assert bob.points == [1, 3]
    assert alice.points == [2, 4]
    assert tim.points == [2]


def test_fans_property(transactions, bob, tim, alice):
    tim + transactions[4]
    assert tim.fans == 1
    bob + transactions[0]
    bob + transactions[0]  # same giver, does not increase fan count
    assert bob.fans == 1
    alice + transactions[1]
    alice + transactions[2]
    assert alice.fans == 2


def test_str_dunder(transactions, bob, tim, alice):
    tim + transactions[4]
    assert str(tim) == 'tim has a karma of 2 and 1 fan'
    alice + transactions[1]
    alice + transactions[3]
    assert str(alice) == 'alice has a karma of 6 and 2 fans'
