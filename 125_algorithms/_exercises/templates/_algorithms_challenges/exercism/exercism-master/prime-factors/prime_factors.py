___ prime_factors(num
    factors =   # list
    i = 2
    w___ i <= num:
        __ num % i __ 0:
            factors.append(i)
            num /= i
        ____
            i += 1
    r_ factors
