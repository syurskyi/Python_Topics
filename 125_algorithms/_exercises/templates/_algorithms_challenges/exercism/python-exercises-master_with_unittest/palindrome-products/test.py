"""
Notes regarding the implementation of smallest_palindrome and
largest_palindrome:

Both functions must take two keyword arguments:
    max_factor -- int
    min_factor -- int, default 0

Their return value must be a tuple (value, factors) where value is the
palindrome itself, and factors is an iterable containing both factors of the
palindrome in arbitrary order.
"""

_______ unittest

____ palindrome_products _______ smallest_palindrome, largest_palindrome


c_ PalindromesTests(unittest.TestCase
    ___ test_largest_palindrome_from_single_digit_factors
        value, factors = largest_palindrome(max_factor=9)
        assertEqual(value, 9)
        assertIn(s..(factors), [{1, 9}, {3, 3}])

    ___ test_largest_palindrome_from_double_digit_factors
        value, factors = largest_palindrome(max_factor=99, min_factor=10)
        assertEqual(value, 9009)
        assertEqual(s..(factors), {91, 99})

    ___ test_smallest_palindrome_from_double_digit_factors
        value, factors = smallest_palindrome(max_factor=99, min_factor=10)
        assertEqual(value, 121)
        assertEqual(s..(factors), {11})

    ___ test_largest_palindrome_from_triple_digit_factors
        value, factors = largest_palindrome(max_factor=999, min_factor=100)
        assertEqual(value, 906609)
        assertEqual(s..(factors), {913, 993})

    ___ test_smallest_palindrome_from_triple_digit_factors
        value, factors = smallest_palindrome(max_factor=999, min_factor=100)
        assertEqual(value, 10201)
        assertEqual(s..(factors), {101, 101})


__ _____ __ _____
    unittest.main()
