_______ threading


c_ BankAccount(object):
    ___ - ):
        is_open = F..
        balance = 0
        lock = threading.Lock()

    ___ get_balance
        with lock:
            __ is_open:
                r.. balance
            ____:
                raise ValueError

    ___ open
        is_open = T..

    ___ deposit(self, amount):
        with lock:
            __ is_open a.. amount > 0:
                balance += amount
            ____:
                raise ValueError

    ___ withdraw(self, amount):
        with lock:
            __ is_open a.. 0 < amount <= balance:
                balance -= amount
            ____:
                raise ValueError

    ___ close
        is_open = F..
