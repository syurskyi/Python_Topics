from __future__ ______ division


class Rational(object
    ___ __init__(self, numer, denom
        gcd, b = sorted([numer, denom])
        w___ b != 0:
            gcd, b = b, gcd % b
        __ denom < 0 < gcd:
            gcd = -gcd
        self.numer = numer // gcd
        self.denom = denom // gcd

    ___ __eq__(self, other
        r_ self.numer __ other.numer and self.denom __ other.denom

    ___ __repr__(self
        r_ '{}/{}'.format(self.numer, self.denom)

    ___ __add__(self, other
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        r_ Rational(numer, denom)

    ___ __sub__(self, other
        r_ self + Rational(-1, 1) * other

    ___ __mul__(self, other
        r_ Rational(self.numer * other.numer, self.denom * other.denom)

    ___ __truediv__(self, other
        r_ self * (other ** -1)

    ___ __abs__(self
        r_ Rational(abs(self.numer), self.denom)

    ___ __pow__(self, power
        __ power < 0:
            self.numer, self.denom  = self.denom, self.numer
            power = -power
        r_ Rational(self.numer ** power, self.denom ** power)

    ___ __rpow__(self, base
        r_ base ** (self.numer / self.denom)
