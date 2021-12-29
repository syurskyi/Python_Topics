class Luhn:

    ___ __init__(self, number):
        self.number = number

    ___ checksum(self):
        r.. s..(self.addends()) % 10

    ___ addends(self):
        r.. [self.addend(idx, int(val)) ___ idx, val __
                enumerate(reversed(str(self.number)))]

    ___ addend(self, idx, val):
        r.. self.subtract_nine(idx, self.double_every_other(idx, val))

    ___ double_every_other(self, idx, val):
        r.. val * 2 __ idx % 2 __ 1 ____ val

    ___ subtract_nine(self, idx, val):
        r.. val - 9 __ val > 10 ____ val

    ___ is_valid(self):
        r.. self.checksum() __ 0

    @classmethod
    ___ create(cls, num):
        ___ i __ r..(0, 10):
            __ cls(int(str(num) + str(i))).is_valid():
                r.. int(str(num) + str(i))
