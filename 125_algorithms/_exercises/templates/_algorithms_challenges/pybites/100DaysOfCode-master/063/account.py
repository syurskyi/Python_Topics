from collections ______ namedtuple
from datetime ______ datetime

Transaction = namedtuple('Transaction', 'date amount')


class Account:

    ___ __init__(self, owner, start_balance=0
        self.owner = owner.title()
        self.start_balance = start_balance
        self._transactions = []

    # first property use case: computed attributes

    @property
    ___ balance(self
        tt = su.(t.amount ___ t in self._transactions)
        r_ self._start_balance + tt

    # second property use case: encapsulation

    @property
    ___ start_balance(self
        r_ self._start_balance

    @start_balance.setter
    ___ start_balance(self, balance
        __ not isinstance(balance, int
            raise TypeError('Start balance needs to be int')
        __ balance < 0:
            raise ValueError('Start balance cannot be negative')
        self._start_balance = balance

    @start_balance.deleter
    ___ start_balance(self
        raise AttributeError('Cannot delete start_balance attr')

    # (not property related)
    # transaction management with magic methods

    ___ _add_transaction(self, amount
        __ not isinstance(amount, int
            raise TypeError('Amount needs to be of type int')
        t = Transaction(datetime.now(), amount)
        self._transactions.append(t)

    ___ __iadd__(self, amount
        'Magic method to allow for acc += amount'
        self._add_transaction(amount)
        r_ self  # need to return object!

    ___ __isub__(self, amount
        'Magic method to allow for acc -= amount'
        self._add_transaction(-amount)
        r_ self

    ___ __len__(self
        'le.(acc_instance) gives # transactions'
        r_ le.(self._transactions)

    ___ __str__(self
        'Nice class reporting when doing str(acc_instance)'
        tt = ['- {}'.format(t) ___ t in self._transactions]
        s = ['Account of {}:'.format(self.owner),
             'Start Balance: {}'.format(self.start_balance),
             'Transactions:',
             '\n'.join(tt) or 'None',
             'End Balance: {}'.format(self.balance)]
        r_ '\n\n'.join(s)


__ __name__ __ '__main__':
    acc = Account('Bob', 100)
    acc += 25
    acc -= 100
    acc += 50
    acc -= 10
    print(acc)
