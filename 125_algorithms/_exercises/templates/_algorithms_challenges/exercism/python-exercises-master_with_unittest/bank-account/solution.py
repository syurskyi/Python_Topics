_______ threading


c_ BankAccount(object):
    ___ - ):
        is_open = F..
        balance = 0
        lock = threading.Lock()

    ___ get_balance
        w__ lock:
            __ is_open:
                r.. balance
            ____:
                r.. ValueError

    ___ open
        is_open = T..

    ___ deposit(self, amount):
        w__ lock:
            __ is_open a.. amount > 0:
                balance += amount
            ____:
                r.. ValueError

    ___ withdraw(self, amount):
        w__ lock:
            __ is_open a.. 0 < amount <= balance:
                balance -= amount
            ____:
                r.. ValueError

    ___ close
        is_open = F..
