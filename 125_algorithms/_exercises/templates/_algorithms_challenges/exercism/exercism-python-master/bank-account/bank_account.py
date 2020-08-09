from threading ______ Lock

class BankAccount(object
    ___ with_lock(lock
        ___ wrapper(func
            ___ wrapped(self, *args
                with getattr(self, lock
                    r_ func(self, *args)
            r_ wrapped
        r_ wrapper

    ___ is_open(func
        ___ wrapped(self, *args
            __ self._state is not 'opened':
                raise ValueError("Account is {}, not open".format(self._state))
            r_ func(self, *args)
        r_ wrapped

    ___ __init__(self
        self._balance = 0
        self._state = 'created'
        self._lock = Lock()

    @is_open
    ___ get_balance(self
        r_ self._balance

    ___ open(self
        self._state = 'opened'

    @is_open
    @with_lock('_lock')
    ___ deposit(self, amount
        __ not (0 <= amount
            raise ValueError("Cannot deposite amount {}".format(amount))
        self._balance += amount

    @is_open
    @with_lock('_lock')
    ___ withdraw(self, amount
        __ not (0 <= amount <= self._balance
            raise ValueError("Cannot withdraw amount {}".format(amount))
        self._balance -= amount

    @is_open
    @with_lock('_lock')
    ___ close(self
        self._state = 'closed'
        r_ self._balance
