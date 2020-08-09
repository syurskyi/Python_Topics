class Account:

    ___ __init__(self
        self._transactions = []

    @property
    ___ balance(self
        r_ su.(self._transactions)

    ___ __add__(self, amount
        __ not isinstance(amount, int
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    ___ __enter__(self
        print('ENTER WITH: making backup of transactions for rollback')
        self._copy_transactions = list(self._transactions)
        r_ self

    ___ __exit__(self, exc_type, exc_val, exc_tb
        print('EXIT WITH:', end=' ')
        __ exc_type:
            self._transactions = self._copy_transactions
            print('rolling back to previous transactions')
            print('transaction {} err ({})'.format(exc_type.__name__, exc_val))
        ____
            print('transaction ok')


___ validate_transaction(acc, amount_to_add
    with acc as a:
        print('adding {} to account'.format(amount_to_add))
        a + amount_to_add
        print('new balance would be: {}'.format(a.balance))
        __ a.balance < 0:
            raise ValueError('sorry cannot go in debt!')


__ __name__ __ '__main__':
    bob = Account()

    # ok transaction
    try:
        validate_transaction(bob, 10)
    except ValueError:
        pass

    print()
    print('balance now: ')
    print(bob.balance)
    print()

    # rollback
    try:
        validate_transaction(bob, -50)
    except ValueError:
        pass

    print()
    print('balance now: ')
    print(bob.balance)
