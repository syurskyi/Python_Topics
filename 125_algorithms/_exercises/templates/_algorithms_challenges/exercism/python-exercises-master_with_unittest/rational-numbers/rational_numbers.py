from __future__ import division


class Rational(object):
    ___ __init__(self, numer, denom):
        self.numer = None
        self.denom = None

    ___ __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    ___ __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    ___ __add__(self, other):
        pass

    ___ __sub__(self, other):
        pass

    ___ __mul__(self, other):
        pass

    ___ __truediv__(self, other):
        pass

    ___ __abs__(self):
        pass

    ___ __pow__(self, power):
        pass

    ___ __rpow__(self, base):
        pass
