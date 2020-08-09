# To avoid trivial solutions, try to solve this problem without the
# function int(s, base=16)

______ unittest

from hexadecimal ______ hexa


class HexadecimalTest(unittest.TestCase

    ___ test_valid_hexa1(self
        self.assertEqual(1, hexa('1'))

    ___ test_valid_hexa2(self
        self.assertEqual(12, hexa('c'))

    ___ test_valid_hexa3(self
        self.assertEqual(16, hexa('10'))

    ___ test_valid_hexa4(self
        self.assertEqual(175, hexa('af'))

    ___ test_valid_hexa5(self
        self.assertEqual(256, hexa('100'))

    ___ test_valid_hexa6(self
        self.assertEqual(105166, hexa('19ACE'))

    ___ test_valid_hexa7(self
        self.assertEqual(0, hexa('000000'))

    ___ test_valid_hexa8(self
        self.assertEqual(16776960, hexa('ffff00'))

    ___ test_valid_hexa9(self
        self.assertEqual(65520, hexa('00fff0'))

    ___ test_invalid_hexa(self
        with self.assertRaises(ValueError
            hexa('carrot')


__ __name__ __ '__main__':
    unittest.main()
