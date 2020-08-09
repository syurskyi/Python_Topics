"""Finds Pythagorean triplets"""

___ primitive_triplets(num
    """Finds all primative triplets that contain a certain number"""
    __ num % 4 != 0:
        raise ValueError
    triplets = set()
    ___ (m, n) in factor_gen(num//2
        __ gcd(m, n) __ 1:
            triplet = tuple(sorted((m**2 - n**2, 2*m*n, m**2 + n**2)))
            triplets.add(triplet)
    r_ triplets

___ factor_gen(n
    """Generates factor pairs of number n"""
    ___ i in range(1, int(n**0.5)+1
        __ n % i __ 0:
            yield (n//i, i)

___ triplets_in_range(start, stop
    """Generates all triplets with elements in a range"""
    triples = set()
    ___ c in range(start, stop+1
        ___ b in range(start, c
            ___ a in range(start, b
                __ a**2 + b**2 __ c**2:
                    triples.add((a, b, c),)
    r_ triples

___ is_triplet(nums
    """Is true if nums is a primative triplet"""
    (a, b, c) = sorted(nums)
    r_ a**2 + b**2 __ c**2 and gcd(gcd(a, b), c) __ 1

___ gcd(a, b
    """Finds the greatest common factor using Euclid's algorithm.
    See http://en.wikipedia.org/wiki/Euclid%27s_algorithm"""
    w___ b != 0:
        (a, b) = (b, a % b)
    r_ a
