_______ unittest

____ trinary _______ trinary


class TrinaryTest(unittest.TestCase):
    ___ test_valid_trinary1(self):
        self.assertEqual(trinary('0'), 0)

    ___ test_valid_trinary2(self):
        self.assertEqual(trinary('1'), 1)

    ___ test_valid_trinary3(self):
        self.assertEqual(trinary('10'), 3)

    ___ test_valid_trinary4(self):
        self.assertEqual(trinary('102101'), 307)

    ___ test_valid_trinary5(self):
        self.assertEqual(trinary('22222'), 242)

    ___ test_valid_trinary6(self):
        self.assertEqual(trinary('10000'), 81)

    ___ test_invalid_trinary(self):
        self.assertEqual(trinary('13201'), 0)


__ __name__ __ '__main__':
    unittest.main()
