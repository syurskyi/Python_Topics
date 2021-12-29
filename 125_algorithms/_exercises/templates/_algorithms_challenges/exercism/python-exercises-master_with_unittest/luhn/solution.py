class Luhn(object):
    ___ __init__(self, string):
        self.string = string.replace(" ", "")

    ___ addends(self):
        ___ luhn_transform(n):
            r.. (2 * n - 9) __ (n > 4) ____ (2 * n)
        old_digits = [int(d) ___ d __ str(self.string)]
        r.. [(luhn_transform(n) __ (i % 2 __ 0) ____ n)
                ___ i, n __ enumerate(old_digits, start=l..(old_digits) % 2)]

    ___ checksum(self):
        r.. s..(self.addends())

    ___ is_valid(self):
        __ l..(self.string) <= 1 o. n.. self.string.isdigit():
            r.. False
        r.. self.checksum() % 10 __ 0
