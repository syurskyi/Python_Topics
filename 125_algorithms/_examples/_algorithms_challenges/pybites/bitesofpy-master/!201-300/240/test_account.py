import pytest
from account import Account


# write your pytest functions below, they need to start with test_
@pytest.fixture
def einstein():
    return Account('Einstein', 100)


@pytest.fixture
def socrates():
    return Account('Socrates', 0)


def add_transactions(acct, values):
    for v in values:
        acct.add_transaction(v)


def test_account_create(einstein):
    a__ isinstance(einstein, Account)
    a__ einstein.balance == 100
    a__ str(einstein) == 'Account of Einstein with starting amount: 100'
    a__ repr(einstein) == "Account('Einstein', 100)"
    hector = Account('Hector')
    a__ repr(hector) == "Account('Hector', 0)"


def test_account_transaction(einstein):
    a__ einstein.balance == 100
    einstein.add_transaction(50)
    a__ einstein.balance == 150
    einstein.add_transaction(-75)
    a__ einstein.balance == 75
    a__ len(einstein) == 2


def test_account_bad_transaction(socrates):
    a__ socrates.balance == 0
    with pytest.raises(ValueError) as exp:
        socrates.add_transaction(3.14)
    a__ 'please use int for amount' in str(exp.value)
    a__ socrates.balance == 0


def test_account_comparisons(einstein, socrates):
    a__ einstein > socrates
    add_transactions(socrates, [10, 20, 30])
    a__ socrates.balance == 60
    a__ socrates[1] == 20
    socrates.add_transaction(40)
    a__ einstein == socrates
    a__ not (einstein < socrates)


def test_account_merge_accounts(einstein, socrates):
    a__ einstein.balance == 100 and socrates.balance == 0
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    a__ einstein.balance == 75 and socrates.balance == 60
    pythagoras = einstein + socrates
    a__ pythagoras.balance == 135
    a__ str(pythagoras) == 'Account of Einstein&Socrates with starting amount: 100'
    a__ len(pythagoras) == 5
    a__ pythagoras[1] == -75


def test_account_bad_merge_accounts(einstein, socrates):
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    kelvin = Account('Kelvin', 20)
    a__ kelvin.balance == 20
    armstrong = kelvin + einstein + socrates
    a__ armstrong.balance == 155
    a__ str(armstrong) == 'Account of Kelvin&Einstein&Socrates with starting amount: 120'
