class Luhn(object
    ___ __init__(self, string
        self.string = string.replace(" ", "")

    ___ addends(self
        ___ luhn_transform(n
            r_ (2 * n - 9) __ (n > 4) else (2 * n)
        old_digits = [int(d) for d in str(self.string)]
        r_ [(luhn_transform(n) __ (i % 2 __ 0) else n)
                for i, n in enumerate(old_digits, start=le.(old_digits) % 2)]

    ___ checksum(self
        r_ sum(self.addends())

    ___ is_valid(self
        __ le.(self.string) <= 1 or not self.string.isdigit(
            r_ False
        r_ self.checksum() % 10 __ 0
