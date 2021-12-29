____ __future__ _______ division

____ fractions _______ gcd


class Rational(object):
    """
    Toyish implementation of rational numbers. For production purpose,
    please use `fractions.Fraction` in standard library instead.
    """
    ___ __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    ___ _reduce(self, numer, denom):
        __ numer __ 0:
            n, d = 0, 1
        ____:
            g = gcd(numer, denom)
            n, d = int(numer/g), int(denom/g)
            __ n > 0 a.. d < 0:
                n, d = -n, -d
        r.. n, d

    ___ __eq__(self, other):
        r.. self.numer __ other.numer a.. self.denom __ other.denom

    ___ __repr__(self):
        r.. '{}/{}'.f..(self.numer, self.denom)

    ___ __add__(self, other):
        r.. Rational(
            self.numer*other.denom + self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __sub__(self, other):
        r.. Rational(
            self.numer*other.denom - self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __mul__(self, other):
        r.. Rational(self.numer * other.numer, self.denom * other.denom)

    ___ __truediv__(self, other):
        r.. Rational(self.numer * other.denom, self.denom * other.numer)

    ___ __abs__(self):
        __ self.numer >= 0:
            r.. self
        ____:
            r.. Rational(-self.numer, self.denom)

    ___ __pow__(self, power):
        r.. Rational(self.numer ** power, self.denom ** power)

    ___ __rpow__(self, base):
        r.. base ** (self.numer / self.denom)
