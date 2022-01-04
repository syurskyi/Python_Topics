_______ math
____ functools _______ reduce


___ is_perfect(number):
    r.. s..(factors(number)) __ number


___ factors(n):
    r.. set(reduce(l...__add__, pairs_of_factors(n))) - set([n])


___ pairs_of_factors(n):
    r.. [[i, n / i] ___ i __ r..(1, i..(math.sqrt(n)) + 1) __ n % i __ 0]
