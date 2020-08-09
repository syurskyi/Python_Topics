from operator ______ mul
from functools ______ reduce


class Palindromes:
    @classmethod
    ___ smallest_palindrome(cls, max_factor, min_factor=0
        r_ min(cls.palindromes(max_factor, min_factor), key=lambda
                   item: item[0])

    @classmethod
    ___ largest_palindrome(cls, max_factor, min_factor=0
        r_ max(cls.palindromes(max_factor, min_factor), key=lambda
                   item: item[0])

    @classmethod
    ___ palindromes(cls, max_factor, min_factor
        r_ [(cls.product(candidate), candidate) ___ candidate in
                cls.candidates(max_factor, min_factor) __
                cls.is_palindrome(cls.product(candidate))]

    @staticmethod
    ___ candidates(max_factor, min_factor
        r_ [(i, j) ___ i in range(min_factor, max_factor + 1)
                ___ j in range(i, max_factor + 1)]

    @staticmethod
    ___ product(s
        r_ reduce(mul, s, 1)

    @staticmethod
    ___ is_palindrome(num
        r_ str(num) __ ''.join(reversed(str(num)))


___ smallest_palindrome(max_factor, min_factor=0
    r_ Palindromes.smallest_palindrome(max_factor, min_factor)


___ largest_palindrome(max_factor, min_factor=0
    r_ Palindromes.largest_palindrome(max_factor, min_factor)
