# To avoid trivial solutions, try to solve this problem without the
# function int(s, base=16)

_______ unittest

____ hexadecimal _______ hexa


c_ HexadecimalTest(unittest.TestCase):
    ___ test_valid_hexa1
        assertEqual(hexa('1'), 1)

    ___ test_valid_hexa2
        assertEqual(hexa('c'), 12)

    ___ test_valid_hexa3
        assertEqual(hexa('10'), 16)

    ___ test_valid_hexa4
        assertEqual(hexa('af'), 175)

    ___ test_valid_hexa5
        assertEqual(hexa('100'), 256)

    ___ test_valid_hexa6
        assertEqual(hexa('19ACE'), 105166)

    ___ test_valid_hexa7
        assertEqual(hexa('000000'), 0)

    ___ test_valid_hexa8
        assertEqual(hexa('ffff00'), 16776960)

    ___ test_valid_hexa9
        assertEqual(hexa('00fff0'), 65520)

    ___ test_invalid_hexa
        with assertRaises(ValueError):
            hexa('carrot')

    ___ test_invalid_empty_string
        with assertRaises(ValueError):
            hexa('')


__ __name__ __ '__main__':
    unittest.main()
