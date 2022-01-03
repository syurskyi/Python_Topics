_______ unittest

____ raindrops _______ raindrops


c_ RaindropsTest(unittest.TestCase):
    ___ test_1
        assertEqual(raindrops(1), "1")

    ___ test_3
        assertEqual(raindrops(3), "Pling")

    ___ test_5
        assertEqual(raindrops(5), "Plang")

    ___ test_7
        assertEqual(raindrops(7), "Plong")

    ___ test_6
        assertEqual(raindrops(6), "Pling")

    ___ test_9
        assertEqual(raindrops(9), "Pling")

    ___ test_10
        assertEqual(raindrops(10), "Plang")

    ___ test_14
        assertEqual(raindrops(14), "Plong")

    ___ test_15
        assertEqual(raindrops(15), "PlingPlang")

    ___ test_21
        assertEqual(raindrops(21), "PlingPlong")

    ___ test_25
        assertEqual(raindrops(25), "Plang")

    ___ test_35
        assertEqual(raindrops(35), "PlangPlong")

    ___ test_49
        assertEqual(raindrops(49), "Plong")

    ___ test_52
        assertEqual(raindrops(52), "52")

    ___ test_105
        assertEqual(raindrops(105), "PlingPlangPlong")

    ___ test_12121
        assertEqual(raindrops(12121), "12121")


__ __name__ __ '__main__':
    unittest.main()
