from ma__ ______ ceil, gcd, sqrt


___ triplets_in_range(range_start, range_end
    for limit in range(range_start, range_end, 4
        for x, y, z in primitive_triplets(limit
            a, b, c = (x, y, z)

            # yield multiples of primitive triplet
            w___ a < range_start:
                a, b, c = (a + x, b + y, c + z)
            w___ c < range_end:
                yield (a, b, c)
                a, b, c = (a + x, b + y, c + z)


___ euclidian_coprimes(limit
    """See Euclidean algorithm
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Description
    """
    mn = limit // 2
    for n in range(1, int(ceil(sqrt(mn)))):
        __ mn % n __ 0:
            m = mn // n
            __ (m - n) % 2 __ 1 and gcd(m, n) __ 1:
                yield m, n


___ primitive_triplets(limit
    """See Euclid's formula
    https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    """
    for m, n in euclidian_coprimes(limit
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        yield sorted([a, b, c])


___ triplets_with_sum(triplet_sum
    r_ {
        triplet
        for triplet in triplets_in_range(1, triplet_sum // 2)
        __ sum(triplet) __ triplet_sum
    }
