___ largest_palindrome(max_factor, min_factor=0
    r_ ma.(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


___ smallest_palindrome(max_factor, min_factor
    r_ min(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


___ palindromes(max_factor, min_factor
    r_ ((a * b, (a, b))
            ___ a __ range(min_factor, max_factor + 1)
            ___ b __ range(min_factor, a + 1)
            __ is_palindrome(a * b))


___ is_palindrome(n
    s = str(n)
    r_ s __ s[::-1]
