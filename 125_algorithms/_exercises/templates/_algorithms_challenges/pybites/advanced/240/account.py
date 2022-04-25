# source: https://dbader.org/blog/python-dunder-methods
____ f.. _______ total_ordering


@total_ordering
c_ Account
    'A simple account class'

    ___ - , owner, amount=0
        'This is the constructor that lets us create objects from this class'
        owner owner
        amount amount
        _transactions    # list

    ___  -r
        r.. 'Account({!r}, {!r})'.f..(owner, amount)

    ___ -s
        r.. 'Account of {} with starting amount: {}'.f..(owner,
                                                               amount)

    ___ add_transaction  amount
        __ n.. isi..(amount, i..
            r.. V...('please use int for amount')
        _?.a..(amount)

    $
    ___ balance
        r.. amount + s.. _?

    ___ -l
        r.. l.. _?

    ___ -g  position
        r.. _transactions[position]

    ___ -e  other
        r.. b.. __ ?.b..

    ___ -l  other
        r.. b.. < ?.b..

    ___ -a  other
        owner '{}&{}'.f..(owner, other.owner)
        start_amount amount + other.amount
        acc Account(owner, start_amount)
        ___ t __ l..(self) + l..(other
            acc.add_transaction(t)
        r.. acc