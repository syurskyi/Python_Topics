___ largest_palindrome(max_factor, min_factor=0
    r_ max(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


___ smallest_palindrome(max_factor, min_factor
    r_ min(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


___ palindromes(max_factor, min_factor
    r_ ((a * b, (a, b))
            for a in range(min_factor, max_factor + 1)
            for b in range(min_factor, a + 1)
            __ is_palindrome(a * b))


___ is_palindrome(n
    s = str(n)
    r_ s __ s[::-1]
