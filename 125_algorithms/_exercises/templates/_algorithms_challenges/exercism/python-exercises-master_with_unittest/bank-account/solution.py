_______ threading


c_ BankAccount(o..
    ___ -
        is_open = F..
        balance = 0
        lock = threading.Lock()

    ___ get_balance
        w__ lock:
            __ is_open:
                r.. balance
            ____
                r.. V...

    ___ open
        is_open = T..

    ___ deposit  amount
        w__ lock:
            __ is_open a.. amount > 0:
                balance += amount
            ____
                r.. V...

    ___ withdraw  amount
        w__ lock:
            __ is_open a.. 0 < amount <= balance:
                balance -= amount
            ____
                r.. V...

    ___ close
        is_open = F..
