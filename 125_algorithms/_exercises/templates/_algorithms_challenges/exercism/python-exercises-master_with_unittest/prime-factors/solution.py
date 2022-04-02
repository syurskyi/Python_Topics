___ prime_factors(number
    factors    # list
    divisor = 2
    w.... number > 1:
        w.... number % divisor __ 0:
            factors.a..(divisor)
            number /= divisor

        divisor += 1

    r.. factors
