c_ Account

    ___ -
        _transactions    # list

    $
    ___ balance
        r.. s.. _?

    ___ -a  amount
        _?.a.. ?)

    ___ -s  amount
        _?.a..(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    ___ -e
        _rollback _?.c..
        r.. _

    ___ __exit__  exc_type, exc_val, exc_tb
        __ exc_type __ n.. N.. o. balance < 0:
            _transactions _rollback
        _rollback N..
        r.. _
