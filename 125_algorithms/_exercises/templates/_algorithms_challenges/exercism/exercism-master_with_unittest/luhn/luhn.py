c_ Luhn:

    ___ - , number
        number = number

    ___ checksum
        r.. s..(addends % 10

    ___ addends
        r.. [addend(idx, i..(val ___ idx, val __
                e..(r..(s..(number)))]

    ___ addend  idx, val
        r.. subtract_nine(idx, double_every_other(idx, val

    ___ double_every_other  idx, val
        r.. val * 2 __ idx % 2 __ 1 ____ val

    ___ subtract_nine  idx, val
        r.. val - 9 __ val > 10 ____ val

    ___ is_valid
        r.. checksum() __ 0

    @classmethod
    ___ create(cls, num
        ___ i __ r..(0, 10
            __ cls(i..(s..(num) + s..(i))).is_valid
                r.. i..(s..(num) + s..(i
