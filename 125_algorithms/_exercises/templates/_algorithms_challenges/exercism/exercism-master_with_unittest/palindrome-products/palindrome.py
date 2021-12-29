____ operator _______ mul
____ functools _______ reduce


class Palindromes:
    @classmethod
    ___ smallest_palindrome(cls, max_factor, min_factor=0):
        r.. m..(cls.palindromes(max_factor, min_factor), key=l....
                   item: item[0])

    @classmethod
    ___ largest_palindrome(cls, max_factor, min_factor=0):
        r.. max(cls.palindromes(max_factor, min_factor), key=l....
                   item: item[0])

    @classmethod
    ___ palindromes(cls, max_factor, min_factor):
        r.. [(cls.product(candidate), candidate) ___ candidate __
                cls.candidates(max_factor, min_factor) __
                cls.is_palindrome(cls.product(candidate))]

    @staticmethod
    ___ candidates(max_factor, min_factor):
        r.. [(i, j) ___ i __ r..(min_factor, max_factor + 1)
                ___ j __ r..(i, max_factor + 1)]

    @staticmethod
    ___ product(s):
        r.. reduce(mul, s, 1)

    @staticmethod
    ___ is_palindrome(num):
        r.. s..(num) __ ''.join(reversed(s..(num)))


___ smallest_palindrome(max_factor, min_factor=0):
    r.. Palindromes.smallest_palindrome(max_factor, min_factor)


___ largest_palindrome(max_factor, min_factor=0):
    r.. Palindromes.largest_palindrome(max_factor, min_factor)
