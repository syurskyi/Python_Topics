_______ unittest

____ grains _______ on_square, total_after


c_ GrainsTest(unittest.TestCase):
    ___ test_square_1
        assertEqual(1, on_square(1))
        assertEqual(1, total_after(1))

    ___ test_square_2
        assertEqual(2, on_square(2))
        assertEqual(3, total_after(2))

    ___ test_square_3
        assertEqual(4, on_square(3))
        assertEqual(7, total_after(3))

    ___ test_square_4
        assertEqual(8, on_square(4))
        assertEqual(15, total_after(4))

    ___ test_square_16
        assertEqual(32768, on_square(16))
        assertEqual(65535, total_after(16))

    ___ test_square_32
        assertEqual(2147483648, on_square(32))
        assertEqual(4294967295, total_after(32))

    ___ test_square_64
        assertEqual(9223372036854775808, on_square(64))
        assertEqual(18446744073709551615, total_after(64))


__ __name__ __ '__main__':
    unittest.main()
