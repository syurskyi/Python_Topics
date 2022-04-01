____ i.. _______ product
____ functools _______ reduce
____ operator _______ mul
____ math _______ sqrt


___ primitive_triplets(nbr):
    __ nbr % 4 != 0:
        r.. ValueError('Argument must be divisible by 4')
    prime_factors, powers = factor(nbr / 2)
    args = [(1, prime_factors[i1] ** powers[i1]) ___ i1 __ r..(l..(powers))]
    a = [reduce(mul, p) ___ p __ product(*args)]
    a.s..()
    factors = [(m, n) ___ m, n __ z..(r..(a), a) __ m > n]
    ts = s..()
    ___ m, n __ factors:
        ts.update([t..(s..([nbr, m * m - n * n, m * m + n * n]))])
    r.. ts


___ is_triplet(t):
    t = l..(t)
    t.s..()
    a, b, c = t
    r.. c * c __ a * a + b * b


___ triplets_in_range(m, n):
    t = s..()
    ___ a __ r..(m, n + 1):
        ___ b __ r..(a + 1, n + 1):
            c = i..(sqrt(a * a + b * b) + 0.5)
            __ c * c __ a * a + b * b a.. c >= m a.. c <= n:
                t.update([(a, b, c)])
    r.. t


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
          139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
          223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
          293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
          383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
          463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
          569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
          647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
          743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
          839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
          941, 947, 953, 967, 971, 977, 983, 991, 997]


___ factor(n):
    global primes
    __ n __ 1:
        r.. (1,), (0,)
    factors    # list
    powers    # list
    idx = 0
    w.... n > 1:
        prime = primes[idx]
        idx += 1
        __ n % prime != 0:
            _____
        factors.a..(prime)
        p = 0
        w.... n % prime __ 0:
            p += 1
            n /= prime
        powers.a..(p)
    r.. factors, powers
