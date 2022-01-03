"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers
      including zero.
    * A list of factors must be given, and its elements are unique
      and sorted in ascending order.
"""

_______ unittest

____ sum_of_multiples _______ sum_of_multiples


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0

c_ SumOfMultiplesTest(unittest.TestCase):
    ___ test_multiples_with_no_factors_in_limit
        assertEqual(sum_of_multiples(1, [3, 5]), 0)

    ___ test_multiples_of_one_factor_within_limit
        assertEqual(sum_of_multiples(4, [3, 5]), 3)

    ___ test_various_multiples_in_limit
        assertEqual(sum_of_multiples(7, [3]), 9)

    ___ test_various_factors_with_multiples_in_limit
        assertEqual(sum_of_multiples(10, [3, 5]), 23)

    ___ test_multiples_counted_only_once
        assertEqual(sum_of_multiples(100, [3, 5]), 2318)

    ___ test_multiples_with_large_limit
        assertEqual(sum_of_multiples(1000, [3, 5]), 233168)

    ___ test_multiples_with_three_factors
        assertEqual(sum_of_multiples(20, [7, 13, 17]), 51)

    ___ test_multiples_with_factors_not_prime
        assertEqual(sum_of_multiples(15, [4, 6]), 30)

    ___ test_multiples_with_factors_prime_and_not
        assertEqual(sum_of_multiples(150, [5, 6, 8]), 4419)

    ___ test_multiples_with_similar_factors
        assertEqual(sum_of_multiples(51, [5, 25]), 275)

    ___ test_multiples_with_large_factors
        assertEqual(sum_of_multiples(10000, [43, 47]), 2203160)

    ___ test_multiples_of_one_will_be_all
        assertEqual(sum_of_multiples(100, [1]), 4950)

    ___ test_multiples_of_an_empty_list
        assertEqual(sum_of_multiples(10000, []), 0)

    ___ test_multiples_of_zero_will_be_none
        assertEqual(sum_of_multiples(1, [0]), 0)

    ___ test_multiples_with_a_zero_factor
        assertEqual(sum_of_multiples(4, [0, 3]), 3)

    ___ test_multiples_of_several_factors
        assertEqual(sum_of_multiples(10000,
                                          [2, 3, 5, 7, 11]), 39614537)


__ __name__ __ '__main__':
    unittest.main()
