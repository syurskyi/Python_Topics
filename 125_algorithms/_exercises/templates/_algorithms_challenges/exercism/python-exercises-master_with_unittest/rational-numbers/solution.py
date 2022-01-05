____ __future__ _______ division

____ fractions _______ gcd


c_ Rational(object):
    """
    Toyish implementation of rational numbers. For production purpose,
    please use `fractions.Fraction` in standard library instead.
    """
    ___ - , numer, denom):
        numer, denom = _reduce(numer, denom)

    ___ _reduce  numer, denom):
        __ numer __ 0:
            n, d = 0, 1
        ____:
            g = gcd(numer, denom)
            n, d = i..(numer/g), i..(denom/g)
            __ n > 0 a.. d < 0:
                n, d = -n, -d
        r.. n, d

    ___ __eq__  other):
        r.. numer __ other.numer a.. denom __ other.denom

    ___ __repr__
        r.. '{}/{}'.f..(numer, denom)

    ___ __add__  other):
        r.. Rational(
            numer*other.denom + denom*other.numer,
            denom*other.denom
        )

    ___ __sub__  other):
        r.. Rational(
            numer*other.denom - denom*other.numer,
            denom*other.denom
        )

    ___ __mul__  other):
        r.. Rational(numer * other.numer, denom * other.denom)

    ___ __truediv__  other):
        r.. Rational(numer * other.denom, denom * other.numer)

    ___ __abs__
        __ numer >= 0:
            r.. self
        ____:
            r.. Rational(-numer, denom)

    ___ __pow__  power):
        r.. Rational(numer ** power, denom ** power)

    ___ __rpow__  base):
        r.. base ** (numer / denom)
