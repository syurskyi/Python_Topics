class Luhn(object):
    ___ __init__(self, string):
        self.string = string.replace(" ", "")

    ___ addends(self):
        ___ luhn_transform(n):
            return (2 * n - 9) __ (n > 4) else (2 * n)
        old_digits = [int(d) for d in str(self.string)]
        return [(luhn_transform(n) __ (i % 2 == 0) else n)
                for i, n in enumerate(old_digits, start=len(old_digits) % 2)]

    ___ checksum(self):
        return sum(self.addends())

    ___ is_valid(self):
        __ len(self.string) <= 1 or not self.string.isdigit():
            return False
        return self.checksum() % 10 == 0
