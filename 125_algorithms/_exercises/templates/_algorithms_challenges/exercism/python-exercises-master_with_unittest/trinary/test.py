_______ unittest

____ trinary _______ trinary


c_ TrinaryTest(unittest.TestCase):
    ___ test_valid_trinary1
        assertEqual(trinary('0'), 0)

    ___ test_valid_trinary2
        assertEqual(trinary('1'), 1)

    ___ test_valid_trinary3
        assertEqual(trinary('10'), 3)

    ___ test_valid_trinary4
        assertEqual(trinary('102101'), 307)

    ___ test_valid_trinary5
        assertEqual(trinary('22222'), 242)

    ___ test_valid_trinary6
        assertEqual(trinary('10000'), 81)

    ___ test_invalid_trinary
        assertEqual(trinary('13201'), 0)


__ __name__ __ '__main__':
    unittest.main()
