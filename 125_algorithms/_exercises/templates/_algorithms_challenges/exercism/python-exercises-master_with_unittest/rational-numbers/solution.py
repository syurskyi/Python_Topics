from __future__ import division

from fractions import gcd


class Rational(object):
    """
    Toyish implementation of rational numbers. For production purpose,
    please use `fractions.Fraction` in standard library instead.
    """
    ___ __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    ___ _reduce(self, numer, denom):
        __ numer == 0:
            n, d = 0, 1
        else:
            g = gcd(numer, denom)
            n, d = int(numer/g), int(denom/g)
            __ n > 0 and d < 0:
                n, d = -n, -d
        return n, d

    ___ __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    ___ __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    ___ __add__(self, other):
        return Rational(
            self.numer*other.denom + self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __sub__(self, other):
        return Rational(
            self.numer*other.denom - self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    ___ __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    ___ __abs__(self):
        __ self.numer >= 0:
            return self
        else:
            return Rational(-self.numer, self.denom)

    ___ __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    ___ __rpow__(self, base):
        return base ** (self.numer / self.denom)
