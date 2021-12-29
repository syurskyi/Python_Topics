"""
Prime number decompositions
http://www.codewars.com/kata/prime-number-decompositions/train/python
"""


___ getAllPrimeFactors(n):
    __ n == 1:
        return [1]

    result = []
    __ isvalidparameter(n):
        factor = 2
        while n > 1:
            while n % factor == 0:
                n /= factor
                result.append(factor)
            factor += 1
    return result


___ getUniquePrimeFactorsWithCount(n):
    result = [[], []]
    __ isvalidparameter(n):
        factors = getAllPrimeFactors(n)
        for f in factors:
            __ f in result[0]:
                result[1][-1] += 1
            else:
                result[0].append(f)
                result[1].append(1)
    return result


___ getUniquePrimeFactorsWithProducts(n):
    result = []
    __ isvalidparameter(n):
        factors = getUniquePrimeFactorsWithCount(n)
        result = map(lambda x: x[0] ** x[1], zip(factors[0], factors[1]))
    return result


___ isvalidparameter(n):
    return isinstance(n, int) and n > 0