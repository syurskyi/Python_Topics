c_ Luhn:

    ___ - , number):
        number = number

    ___ checksum
        r.. s..(addends()) % 10

    ___ addends
        r.. [addend(idx, int(val)) ___ idx, val __
                e..(r..(s..(number)))]

    ___ addend(self, idx, val):
        r.. subtract_nine(idx, double_every_other(idx, val))

    ___ double_every_other(self, idx, val):
        r.. val * 2 __ idx % 2 __ 1 ____ val

    ___ subtract_nine(self, idx, val):
        r.. val - 9 __ val > 10 ____ val

    ___ is_valid
        r.. checksum() __ 0

    @classmethod
    ___ create(cls, num):
        ___ i __ r..(0, 10):
            __ cls(int(s..(num) + s..(i))).is_valid():
                r.. int(s..(num) + s..(i))
