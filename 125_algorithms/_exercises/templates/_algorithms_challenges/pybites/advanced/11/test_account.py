_______ p__

____ account _______ Account

checking Account('Checking')
saving Account('Saving', 10)


___ test_account_balance
    ... checking.start_balance __ 0
    checking + 10
    ... checking.balance __ 10

    ... saving.start_balance __ 10
    w__ p__.r.. T..
        saving - 'a'
    saving - 5
    ... saving.balance __ 5


___ test_account_comparison
    ... checking > saving
    ... checking >_ saving
    ... saving < checking
    ... saving <_ checking
    saving + 5
    ... checking __ saving


___ test_account_len
    checking + 10
    checking + 3
    checking - 8
    ... l..(checking) __ 4


___ test_account_indexing_iter
    ... checking[0] __ 10
    ... checking[-1] __ -8
    ... l..(checking) __ [10, 10, 3, -8]


___ test_account_str
    ... s..(checking) __ 'Checking account - balance: 15'
    ... s..(saving) __ 'Saving account - balance: 10'
    saving + 5
    ... s..(saving) __ 'Saving account - balance: 15'