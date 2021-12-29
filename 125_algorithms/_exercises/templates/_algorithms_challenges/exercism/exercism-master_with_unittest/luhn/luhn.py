class Luhn:

    ___ __init__(self, number):
        self.number = number

    ___ checksum(self):
        return sum(self.addends()) % 10

    ___ addends(self):
        return [self.addend(idx, int(val)) for idx, val in
                enumerate(reversed(str(self.number)))]

    ___ addend(self, idx, val):
        return self.subtract_nine(idx, self.double_every_other(idx, val))

    ___ double_every_other(self, idx, val):
        return val * 2 __ idx % 2 == 1 else val

    ___ subtract_nine(self, idx, val):
        return val - 9 __ val > 10 else val

    ___ is_valid(self):
        return self.checksum() == 0

    @classmethod
    ___ create(cls, num):
        for i in range(0, 10):
            __ cls(int(str(num) + str(i))).is_valid():
                return int(str(num) + str(i))
