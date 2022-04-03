# To avoid trivial solutions, try to solve this problem without the
# function int(s, base=16)

_______ unittest

____ hexadecimal _______ hexa


c_ HexadecimalTest(unittest.TestCase

    ___ test_valid_hexa1
        assertEqual(1, hexa('1'))

    ___ test_valid_hexa2
        assertEqual(12, hexa('c'))

    ___ test_valid_hexa3
        assertEqual(16, hexa('10'))

    ___ test_valid_hexa4
        assertEqual(175, hexa('af'))

    ___ test_valid_hexa5
        assertEqual(256, hexa('100'))

    ___ test_valid_hexa6
        assertEqual(105166, hexa('19ACE'))

    ___ test_valid_hexa7
        assertEqual(0, hexa('000000'))

    ___ test_valid_hexa8
        assertEqual(16776960, hexa('ffff00'))

    ___ test_valid_hexa9
        assertEqual(65520, hexa('00fff0'))

    ___ test_invalid_hexa
        w__ assertRaises(V...
            hexa('carrot')


__ _____ __ _____
    unittest.main()
