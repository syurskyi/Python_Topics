___ prime_factors(num):
    factors = []
    i = 2
    while i <= num:
        __ num % i == 0:
            factors.append(i)
            num /= i
        else:
            i += 1
    return factors
