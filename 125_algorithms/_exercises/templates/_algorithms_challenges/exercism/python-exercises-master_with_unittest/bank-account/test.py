_______ sys
_______ threading
_______ time
_______ unittest

____ bank_account _______ BankAccount


c_ BankAccountTest(unittest.TestCase):

    ___ setUp
        account = BankAccount()

    ___ test_newly_opened_account_has_zero_balance
        account.open()
        assertEqual(account.get_balance(), 0)

    ___ test_can_deposit_money
        account.open()
        account.deposit(100)
        assertEqual(account.get_balance(), 100)

    ___ test_can_deposit_money_sequentially
        account.open()
        account.deposit(100)
        account.deposit(50)

        assertEqual(account.get_balance(), 150)

    ___ test_can_withdraw_money
        account.open()
        account.deposit(100)
        account.withdraw(50)

        assertEqual(account.get_balance(), 50)

    ___ test_can_withdraw_money_sequentially
        account.open()
        account.deposit(100)
        account.withdraw(20)
        account.withdraw(80)

        assertEqual(account.get_balance(), 0)

    ___ test_checking_balance_of_closed_account_throws_error
        account.open()
        account.close()

        with assertRaises(ValueError):
            account.get_balance()

    ___ test_deposit_into_closed_account
        account.open()
        account.close()

        with assertRaises(ValueError):
            account.deposit(50)

    ___ test_withdraw_from_closed_account
        account.open()
        account.close()

        with assertRaises(ValueError):
            account.withdraw(50)

    ___ test_cannot_withdraw_more_than_deposited
        account.open()
        account.deposit(25)

        with assertRaises(ValueError):
            account.withdraw(50)

    ___ test_cannot_withdraw_negative
        account.open()
        account.deposit(100)

        with assertRaises(ValueError):
            account.withdraw(-50)

    ___ test_cannot_deposit_negative
        account.open()

        with assertRaises(ValueError):
            account.deposit(-50)

    ___ test_can_handle_concurrent_transactions
        account.open()
        account.deposit(1000)

        ___ _ __ r..(10):
            adjust_balance_concurrently()

    ___ adjust_balance_concurrently
        ___ transact():
            account.deposit(5)
            time.sleep(0.001)
            account.withdraw(5)

        # Greatly improve the chance of an operation being interrupted
        # by thread switch, thus testing synchronization effectively
        try:
            sys.setswitchinterval(1e-12)
        except AttributeError:
            # For Python 2 compatibility
            sys.setcheckinterval(1)

        threads    # list
        ___ _ __ r..(1000):
            t = threading.Thread(target=transact)
            threads.a..(t)
            t.start()

        ___ thread __ threads:
            thread.j..()

        assertEqual(account.get_balance(), 1000)


__ __name__ __ '__main__':
    unittest.main()
