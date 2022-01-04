c_ Luhn(object):
    ___ - , s__):
        s__ = s__.r..(" ", "")

    ___ addends
        ___ luhn_transform(n):
            r.. (2 * n - 9) __ (n > 4) ____ (2 * n)
        old_digits = [i..(d) ___ d __ s..(s__)]
        r.. [(luhn_transform(n) __ (i % 2 __ 0) ____ n)
                ___ i, n __ e..(old_digits, start=l..(old_digits) % 2)]

    ___ checksum
        r.. s..(addends())

    ___ is_valid
        __ l..(s__) <= 1 o. n.. s__.isdigit
            r.. F..
        r.. checksum() % 10 __ 0
