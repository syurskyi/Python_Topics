____ o.. _______ mul
____ f.. _______ r..


c_ Palindromes:
    @classmethod
    ___ smallest_palindrome(cls, max_factor, min_factor=0
        r.. m..(cls.palindromes(max_factor, min_factor), key=l....
                   item: item[0])

    @classmethod
    ___ largest_palindrome(cls, max_factor, min_factor=0
        r.. m..(cls.palindromes(max_factor, min_factor), key=l....
                   item: item[0])

    @classmethod
    ___ palindromes(cls, max_factor, min_factor
        r.. [(cls.product(candidate), candidate) ___ candidate __
                cls.candidates(max_factor, min_factor) __
                cls.is_palindrome(cls.product(candidate]

    $
    ___ candidates(max_factor, min_factor
        r.. [(i, j) ___ i __ r..(min_factor, max_factor + 1)
                ___ j __ r..(i, max_factor + 1)]

    $
    ___ product(s
        r.. r.. mul, s, 1)

    $
    ___ is_palindrome(num
        r.. s..(num) __ ''.j..(r..(s..(num)))


___ smallest_palindrome(max_factor, min_factor=0
    r.. Palindromes.smallest_palindrome(max_factor, min_factor)


___ largest_palindrome(max_factor, min_factor=0
    r.. Palindromes.largest_palindrome(max_factor, min_factor)
