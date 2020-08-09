from __future__ ______ division

from fractions ______ gcd


class Rational(object
    """
    Toyish implementation of rational numbers. For production purpose,
    please use `fractions.Fraction` in standard library instead.
    """
    ___ __init__(self, numer, denom
        self.numer, self.denom = self._reduce(numer, denom)

    ___ _reduce(self, numer, denom
        __ numer __ 0:
            n, d = 0, 1
        ____
            g = gcd(numer, denom)
            n, d = int(numer/g), int(denom/g)
            __ n > 0 and d < 0:
                n, d = -n, -d
        r_ n, d

    ___ __eq__(self, other
        r_ self.numer __ other.numer and self.denom __ other.denom

    ___ __repr__(self
        r_ '{}/{}'.format(self.numer, self.denom)

    ___ __add__(self, other
        r_ Rational(
            self.numer*other.denom + self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __sub__(self, other
        r_ Rational(
            self.numer*other.denom - self.denom*other.numer,
            self.denom*other.denom
        )

    ___ __mul__(self, other
        r_ Rational(self.numer * other.numer, self.denom * other.denom)

    ___ __truediv__(self, other
        r_ Rational(self.numer * other.denom, self.denom * other.numer)

    ___ __abs__(self
        __ self.numer >= 0:
            r_ self
        ____
            r_ Rational(-self.numer, self.denom)

    ___ __pow__(self, power
        r_ Rational(self.numer ** power, self.denom ** power)

    ___ __rpow__(self, base
        r_ base ** (self.numer / self.denom)
