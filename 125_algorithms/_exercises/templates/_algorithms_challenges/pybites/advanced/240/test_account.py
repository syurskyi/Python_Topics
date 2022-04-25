_______ p__
____ ? _______ ?


# write your pytest functions below, they need to start with test_
?p__.f..
___ einstein
    r.. Account('Einstein', 100)


?p__.f..
___ socrates
    r.. Account('Socrates', 0)


___ add_transactions(acct, values
    ___ v __ values:
        acct.add_transaction(v)


___ test_account_create(einstein
    ... isi..(einstein, Account)
    ... einstein.balance __ 100
    ... s..(einstein) __ 'Account of Einstein with starting amount: 100'
    ... r.. (einstein) __ "Account('Einstein', 100)"
    hector Account('Hector')
    ... r.. (hector) __ "Account('Hector', 0)"


___ test_account_transaction(einstein
    ... einstein.balance __ 100
    einstein.add_transaction(50)
    ... einstein.balance __ 150
    einstein.add_transaction(-75)
    ... einstein.balance __ 75
    ... l..(einstein) __ 2


___ test_account_bad_transaction(socrates
    ... socrates.balance __ 0
    w__ p__.r..(V...) __ exp:
        socrates.add_transaction(3.14)
    ... 'please use int for amount' __ s..(exp.v..)
    ... socrates.balance __ 0


___ test_account_comparisons(einstein, socrates
    ... einstein > socrates
    add_transactions(socrates, [10, 20, 30])
    ... socrates.balance __ 60
    ... socrates[1] __ 20
    socrates.add_transaction(40)
    ... einstein __ socrates
    ... n.. (einstein < socrates)


___ test_account_merge_accounts(einstein, socrates
    ... einstein.balance __ 100 a.. socrates.balance __ 0
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    ... einstein.balance __ 75 a.. socrates.balance __ 60
    pythagoras einstein + socrates
    ... pythagoras.balance __ 135
    ... s..(pythagoras) __ 'Account of Einstein&Socrates with starting amount: 100'
    ... l..(pythagoras) __ 5
    ... pythagoras[1] __ -75


___ test_account_bad_merge_accounts(einstein, socrates
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    kelvin Account('Kelvin', 20)
    ... kelvin.balance __ 20
    armstrong kelvin + einstein + socrates
    ... armstrong.balance __ 155
    ... s..(armstrong) __ 'Account of Kelvin&Einstein&Socrates with starting amount: 120'
