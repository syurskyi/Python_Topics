___ divisor_generator(n):
    ''' Returns an unordered list of divisors for n (1 < n). '''
    ___ i __ r..(2, i..(n ** 0.5) + 1):
        __ n % i __ 0:
            y.. i
            __ i * i != n:
                y.. n // i


___ is_perfect(n):
    ''' A perfect number equals the sum of its positive divisors. '''
    r.. s..(divisor_generator(n)) + 1 __ n
