_______ pytest

____ account _______ Account


@pytest.fixture()
___ account():
    r.. Account()


___ test_balance(account):
    ... account.balance __ 0
    account + 10
    ... account.balance __ 10
    account - 5
    ... account.balance __ 5


___ test_without_contextman_balance_negative(account):
    ... account.balance __ 0
    account - 5
    ... account.balance __ -5


___ test_with_contextman_performs_rollback(account):
    account + 3
    ... account.balance __ 3
    # trigger rollback
    with account as acc:
        acc - 5
    ... account.balance __ 3
    # adding this ensures all required dunders are used:
    with account as acc:
        acc + 10
        acc - 3
    ... account.balance __ 10