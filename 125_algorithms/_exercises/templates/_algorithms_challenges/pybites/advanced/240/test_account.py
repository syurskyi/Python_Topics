_______ pytest
____ account _______ Account


# write your pytest functions below, they need to start with test_
@pytest.fixture
___ einstein():
    r.. Account('Einstein', 100)


@pytest.fixture
___ socrates():
    r.. Account('Socrates', 0)


___ add_transactions(acct, values):
    ___ v __ values:
        acct.add_transaction(v)


___ test_account_create(einstein):
    ... isi..(einstein, Account)
    ... einstein.balance __ 100
    ... str(einstein) __ 'Account of Einstein with starting amount: 100'
    ... repr(einstein) __ "Account('Einstein', 100)"
    hector = Account('Hector')
    ... repr(hector) __ "Account('Hector', 0)"


___ test_account_transaction(einstein):
    ... einstein.balance __ 100
    einstein.add_transaction(50)
    ... einstein.balance __ 150
    einstein.add_transaction(-75)
    ... einstein.balance __ 75
    ... l..(einstein) __ 2


___ test_account_bad_transaction(socrates):
    ... socrates.balance __ 0
    with pytest.raises(ValueError) as exp:
        socrates.add_transaction(3.14)
    ... 'please use int for amount' __ str(exp.value)
    ... socrates.balance __ 0


___ test_account_comparisons(einstein, socrates):
    ... einstein > socrates
    add_transactions(socrates, [10, 20, 30])
    ... socrates.balance __ 60
    ... socrates[1] __ 20
    socrates.add_transaction(40)
    ... einstein __ socrates
    ... n.. (einstein < socrates)


___ test_account_merge_accounts(einstein, socrates):
    ... einstein.balance __ 100 and socrates.balance __ 0
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    ... einstein.balance __ 75 and socrates.balance __ 60
    pythagoras = einstein + socrates
    ... pythagoras.balance __ 135
    ... str(pythagoras) __ 'Account of Einstein&Socrates with starting amount: 100'
    ... l..(pythagoras) __ 5
    ... pythagoras[1] __ -75


___ test_account_bad_merge_accounts(einstein, socrates):
    add_transactions(einstein, [50, -75])
    add_transactions(socrates, [10, 20, 30])
    kelvin = Account('Kelvin', 20)
    ... kelvin.balance __ 20
    armstrong = kelvin + einstein + socrates
    ... armstrong.balance __ 155
    ... str(armstrong) __ 'Account of Kelvin&Einstein&Socrates with starting amount: 120'
