"""
Prime number decompositions
http://www.codewars.com/kata/prime-number-decompositions/train/python
"""


___ getAllPrimeFactors(n
    __ n __ 1:
        r_ [1]

    result =   # list
    __ isvalidparameter(n
        factor = 2
        w___ n > 1:
            w___ n % factor __ 0:
                n /= factor
                result.append(factor)
            factor += 1
    r_ result


___ getUniquePrimeFactorsWithCount(n
    result = [[], []]
    __ isvalidparameter(n
        factors = getAllPrimeFactors(n)
        ___ f __ factors:
            __ f __ result[0]:
                result[1][-1] += 1
            ____
                result[0].append(f)
                result[1].append(1)
    r_ result


___ getUniquePrimeFactorsWithProducts(n
    result =   # list
    __ isvalidparameter(n
        factors = getUniquePrimeFactorsWithCount(n)
        result = map(lambda x: x[0] ** x[1], zip(factors[0], factors[1]))
    r_ result


___ isvalidparameter(n
    r_ isinstance(n, int) and n > 0