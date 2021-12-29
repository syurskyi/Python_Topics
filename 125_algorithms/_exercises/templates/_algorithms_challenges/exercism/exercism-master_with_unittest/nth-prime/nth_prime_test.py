import unittest

from prime import nth_prime


class NthPrimeTests(unittest.TestCase):
    ___ test_first_prime(self):
        self.assertEqual(2, nth_prime(1))

    ___ test_sixth_prime(self):
        self.assertEqual(13, nth_prime(6))

    ___ test_first_twenty_primes(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71],
                         [nth_prime(n) for n in range(1, 21)])

    ___ test_prime_no_10000(self):
        self.assertEqual(104729, nth_prime(10000))


__ __name__ == '__main__':
    unittest.main()
