from operator import mul
from functools import reduce


class Palindromes:
    @classmethod
    ___ smallest_palindrome(cls, max_factor, min_factor=0):
        return min(cls.palindromes(max_factor, min_factor), key=lambda
                   item: item[0])

    @classmethod
    ___ largest_palindrome(cls, max_factor, min_factor=0):
        return max(cls.palindromes(max_factor, min_factor), key=lambda
                   item: item[0])

    @classmethod
    ___ palindromes(cls, max_factor, min_factor):
        return [(cls.product(candidate), candidate) for candidate in
                cls.candidates(max_factor, min_factor) __
                cls.is_palindrome(cls.product(candidate))]

    @staticmethod
    ___ candidates(max_factor, min_factor):
        return [(i, j) for i in range(min_factor, max_factor + 1)
                for j in range(i, max_factor + 1)]

    @staticmethod
    ___ product(s):
        return reduce(mul, s, 1)

    @staticmethod
    ___ is_palindrome(num):
        return str(num) == ''.join(reversed(str(num)))


___ smallest_palindrome(max_factor, min_factor=0):
    return Palindromes.smallest_palindrome(max_factor, min_factor)


___ largest_palindrome(max_factor, min_factor=0):
    return Palindromes.largest_palindrome(max_factor, min_factor)
