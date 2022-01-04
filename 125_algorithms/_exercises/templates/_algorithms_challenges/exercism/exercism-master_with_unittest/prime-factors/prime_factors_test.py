_______ unittest

____ prime_factors _______ prime_factors


c_ PrimeFactorsTest(unittest.TestCase):
    ___ test_1
        assertEqual([], prime_factors(1))

    ___ test_2
        assertEqual([2], prime_factors(2))

    ___ test_3
        assertEqual([3], prime_factors(3))

    ___ test_4
        assertEqual([2, 2], prime_factors(4))

    ___ test_6
        assertEqual([2, 3], prime_factors(6))

    ___ test_8
        assertEqual([2, 2, 2], prime_factors(8))

    ___ test_9
        assertEqual([3, 3], prime_factors(9))

    ___ test_27
        assertEqual([3, 3, 3], prime_factors(27))

    ___ test_625
        assertEqual([5, 5, 5, 5], prime_factors(625))

    ___ test_901255
        assertEqual([5, 17, 23, 461], prime_factors(901255))

    ___ test_93819012551
        assertEqual([11, 9539, 894119], prime_factors(93819012551))


__ _____ __ _____
    unittest.main()
