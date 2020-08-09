______ pytest

from Previous.account ______ Account


@pytest.fixture()
___ account(
    r_ Account()


___ test_balance(account
    assert account.balance __ 0
    account + 10
    assert account.balance __ 10
    account - 5
    assert account.balance __ 5


___ test_without_contextman_balance_negative(account
    assert account.balance __ 0
    account - 5
    assert account.balance __ -5


___ test_with_contextman_performs_rollback(account
    assert account.balance __ 0
    with account as acc:
        acc - 5
        acc - 5
    assert account.balance __ 0
    # adding this ensures all required dunders are used:
    with account as acc:
        acc + 10
    assert account.balance __ 10