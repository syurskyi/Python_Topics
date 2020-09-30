______ unittest

from prime_factors ______ prime_factors


class PrimeFactorsTest(unittest.TestCase
    ___ test_1(self
        self.assertEqual(  # list, prime_factors(1))

    ___ test_2(self
        self.assertEqual([2], prime_factors(2))

    ___ test_3(self
        self.assertEqual([3], prime_factors(3))

    ___ test_4(self
        self.assertEqual([2, 2], prime_factors(4))

    ___ test_6(self
        self.assertEqual([2, 3], prime_factors(6))

    ___ test_8(self
        self.assertEqual([2, 2, 2], prime_factors(8))

    ___ test_9(self
        self.assertEqual([3, 3], prime_factors(9))

    ___ test_27(self
        self.assertEqual([3, 3, 3], prime_factors(27))

    ___ test_625(self
        self.assertEqual([5, 5, 5, 5], prime_factors(625))

    ___ test_901255(self
        self.assertEqual([5, 17, 23, 461], prime_factors(901255))

    ___ test_93819012551(self
        self.assertEqual([11, 9539, 894119], prime_factors(93819012551))

__  -n __ '__main__':
    unittest.main()
