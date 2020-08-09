___ divisor_generator(n
    ''' Returns an unordered list of divisors for n (1 < n). '''
    for i in range(2, int(n ** 0.5) + 1
        __ n % i __ 0:
            yield i
            __ i * i != n:
                yield n // i


___ is_perfect(n
    ''' A perfect number equals the sum of its positive divisors. '''
    r_ sum(divisor_generator(n)) + 1 __ n
