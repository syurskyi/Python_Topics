import pytest

from Previous.account import Account


@pytest.fixture()
def account():
    return Account()


def test_balance(account):
    a__ account.balance == 0
    account + 10
    a__ account.balance == 10
    account - 5
    a__ account.balance == 5


def test_without_contextman_balance_negative(account):
    a__ account.balance == 0
    account - 5
    a__ account.balance == -5


def test_with_contextman_performs_rollback(account):
    a__ account.balance == 0
    with account as acc:
        acc - 5
        acc - 5
    a__ account.balance == 0
    # adding this ensures all required dunders are used:
    with account as acc:
        acc + 10
    a__ account.balance == 10