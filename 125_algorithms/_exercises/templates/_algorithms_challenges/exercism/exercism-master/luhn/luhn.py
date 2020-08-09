class Luhn:

    ___ __init__(self, number
        self.number = number

    ___ checksum(self
        r_ su.(self.addends()) % 10

    ___ addends(self
        r_ [self.addend(idx, int(val)) ___ idx, val in
                enumerate(reversed(str(self.number)))]

    ___ addend(self, idx, val
        r_ self.subtract_nine(idx, self.double_every_other(idx, val))

    ___ double_every_other(self, idx, val
        r_ val * 2 __ idx % 2 __ 1 else val

    ___ subtract_nine(self, idx, val
        r_ val - 9 __ val > 10 else val

    ___ is_valid(self
        r_ self.checksum() __ 0

    @classmethod
    ___ create(cls, num
        ___ i in range(0, 10
            __ cls(int(str(num) + str(i))).is_valid(
                r_ int(str(num) + str(i))
