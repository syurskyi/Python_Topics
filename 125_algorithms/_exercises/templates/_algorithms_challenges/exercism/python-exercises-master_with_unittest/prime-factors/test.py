_______ unittest

____ prime_factors _______ prime_factors


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ PrimeFactorsTest(unittest.TestCase):
    ___ test_no_factors
        assertEqual(prime_factors(1), [])

    ___ test_prime_number
        assertEqual(prime_factors(2), [2])

    ___ test_square_of_a_prime
        assertEqual(prime_factors(9), [3, 3])

    ___ test_cube_of_a_prime
        assertEqual(prime_factors(8), [2, 2, 2])

    ___ test_product_of_primes_and_non_primes
        assertEqual(prime_factors(12), [2, 2, 3])

    ___ test_product_of_primes
        assertEqual(prime_factors(901255), [5, 17, 23, 461])

    ___ test_factors_include_a_large_prime
        assertEqual(prime_factors(93819012551), [11, 9539, 894119])


__ __name__ __ '__main__':
    unittest.main()
