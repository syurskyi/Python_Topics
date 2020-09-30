"""Finds the prime factors of a number"""

___ prime_factors(number
    """Finds prime factors of a number"""
    factors =   # list
    ___ factor __ range(2, int(number**0.5)+1
        w___ number % factor __ 0:
            number /= factor
            factors.append(factor)
            __ number __ 1:
                break
    __ number != 1:
        factors += [number]
    r_ factors

