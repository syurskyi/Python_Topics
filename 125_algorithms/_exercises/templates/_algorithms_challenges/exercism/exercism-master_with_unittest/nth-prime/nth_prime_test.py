_______ unittest

____ prime _______ nth_prime


c_ NthPrimeTests(unittest.TestCase
    ___ test_first_prime
        assertEqual(2, nth_prime(1

    ___ test_sixth_prime
        assertEqual(13, nth_prime(6

    ___ test_first_twenty_primes
        assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71],
                         [nth_prime(n) ___ n __ r..(1, 21)])

    ___ test_prime_no_10000
        assertEqual(104729, nth_prime(10000


__ _____ __ _____
    unittest.main()
