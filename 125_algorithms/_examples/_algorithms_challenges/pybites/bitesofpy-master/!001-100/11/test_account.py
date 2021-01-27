import pytest

from account import Account

checking = Account('Checking')
saving = Account('Saving', 10)


def test_account_balance():
    a__ checking.start_balance == 0
    checking + 10
    a__ checking.balance == 10

    a__ saving.start_balance == 10
    with pytest.raises(ValueError):
        saving - 'a'
    saving - 5
    a__ saving.balance == 5


def test_account_comparison():
    a__ checking > saving
    a__ checking >= saving
    a__ saving < checking
    a__ saving <= checking
    saving + 5
    a__ checking == saving


def test_account_len():
    checking + 10
    checking + 3
    checking - 8
    a__ len(checking) == 4


def test_account_indexing_iter():
    a__ checking[0] == 10
    a__ checking[-1] == -8
    a__ list(checking) == [10, 10, 3, -8]


def test_account_str():
    a__ str(checking) == 'Checking account - balance: 15'
    a__ str(saving) == 'Saving account - balance: 10'
    saving + 5
    a__ str(saving) == 'Saving account - balance: 15'