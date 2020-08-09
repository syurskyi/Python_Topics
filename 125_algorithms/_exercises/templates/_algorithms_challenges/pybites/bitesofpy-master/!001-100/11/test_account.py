______ pytest

from account ______ Account

checking = Account('Checking')
saving = Account('Saving', 10)


___ test_account_balance(
    assert checking.start_balance __ 0
    checking + 10
    assert checking.balance __ 10

    assert saving.start_balance __ 10
    with pytest.raises(ValueError
        saving - 'a'
    saving - 5
    assert saving.balance __ 5


___ test_account_comparison(
    assert checking > saving
    assert checking >= saving
    assert saving < checking
    assert saving <= checking
    saving + 5
    assert checking __ saving


___ test_account_len(
    checking + 10
    checking + 3
    checking - 8
    assert le.(checking) __ 4


___ test_account_indexing_iter(
    assert checking[0] __ 10
    assert checking[-1] __ -8
    assert list(checking) __ [10, 10, 3, -8]


___ test_account_str(
    assert str(checking) __ 'Checking account - balance: 15'
    assert str(saving) __ 'Saving account - balance: 10'
    saving + 5
    assert str(saving) __ 'Saving account - balance: 15'