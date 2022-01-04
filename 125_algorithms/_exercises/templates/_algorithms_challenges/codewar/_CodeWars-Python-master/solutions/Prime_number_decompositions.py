"""
Prime number decompositions
http://www.codewars.com/kata/prime-number-decompositions/train/python
"""


___ getAllPrimeFactors(n):
    __ n __ 1:
        r.. [1]

    result    # list
    __ isvalidparameter(n):
        factor = 2
        w.... n > 1:
            w.... n % factor __ 0:
                n /= factor
                result.a..(factor)
            factor += 1
    r.. result


___ getUniquePrimeFactorsWithCount(n):
    result = [[], []]
    __ isvalidparameter(n):
        factors = getAllPrimeFactors(n)
        ___ f __ factors:
            __ f __ result[0]:
                result[1][-1] += 1
            ____:
                result[0].a..(f)
                result[1].a..(1)
    r.. result


___ getUniquePrimeFactorsWithProducts(n):
    result    # list
    __ isvalidparameter(n):
        factors = getUniquePrimeFactorsWithCount(n)
        result = map(l.... x: x[0] ** x[1], z..(factors[0], factors[1]))
    r.. result


___ isvalidparameter(n):
    r.. isi..(n, i..) a.. n > 0