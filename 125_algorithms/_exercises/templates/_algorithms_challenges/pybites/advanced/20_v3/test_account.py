_______ p__

____ Previous.account _______ Account


?p__.f..()
___ account
    r.. Account()


___ test_balance(account
    ... account.balance __ 0
    account + 10
    ... account.balance __ 10
    account - 5
    ... account.balance __ 5


___ test_without_contextman_balance_negative(account
    ... account.balance __ 0
    account - 5
    ... account.balance __ -5


___ test_with_contextman_performs_rollback(account
    ... account.balance __ 0
    w__ account __ acc:
        acc - 5
        acc - 5
    ... account.balance __ 0
    # adding this ensures all required dunders are used:
    w__ account __ acc:
        acc + 10
    ... account.balance __ 10