____ math _______ ceil, gcd, sqrt


___ triplets_in_range(range_start, range_end):
    ___ limit __ r..(range_start, range_end, 4):
        ___ x, y, z __ primitive_triplets(limit):
            a, b, c = (x, y, z)

            # yield multiples of primitive triplet
            while a < range_start:
                a, b, c = (a + x, b + y, c + z)
            while c < range_end:
                yield (a, b, c)
                a, b, c = (a + x, b + y, c + z)


___ euclidian_coprimes(limit):
    """See Euclidean algorithm
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Description
    """
    mn = limit // 2
    ___ n __ r..(1, int(ceil(sqrt(mn)))):
        __ mn % n __ 0:
            m = mn // n
            __ (m - n) % 2 __ 1 and gcd(m, n) __ 1:
                yield m, n


___ primitive_triplets(limit):
    """See Euclid's formula
    https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    """
    ___ m, n __ euclidian_coprimes(limit):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        yield s..([a, b, c])


___ triplets_with_sum(triplet_sum):
    r.. {
        triplet
        ___ triplet __ triplets_in_range(1, triplet_sum // 2)
        __ s..(triplet) __ triplet_sum
    }
