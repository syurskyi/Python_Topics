_______ unittest

____ nth_prime _______ nth_prime


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ NthPrimeTests(unittest.TestCase):
    ___ test_first_prime
        assertEqual(nth_prime(1), 2)

    ___ test_second_prime
        assertEqual(nth_prime(2), 3)

    ___ test_sixth_prime
        assertEqual(nth_prime(6), 13)

    ___ test_big_prime
        assertEqual(nth_prime(10001), 104743)

    ___ test_there_is_no_zeroth_prime
        w__ assertRaises(ValueError):
            nth_prime(0)

    # additional track specific test
    ___ test_first_twenty_primes
        assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71],
                         [nth_prime(n) ___ n __ r..(1, 21)])


__ _____ __ _____
    unittest.main()
