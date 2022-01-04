_______ unittest

____ grains _______ (
    on_square,
    total_after,
)


c_ GrainsTest(unittest.TestCase):
    ___ test_square_1
        assertEqual(on_square(1), 1)
        assertEqual(total_after(1), 1)

    ___ test_square_2
        assertEqual(on_square(2), 2)
        assertEqual(total_after(2), 3)

    ___ test_square_3
        assertEqual(on_square(3), 4)
        assertEqual(total_after(3), 7)

    ___ test_square_4
        assertEqual(on_square(4), 8)
        assertEqual(total_after(4), 15)

    ___ test_square_16
        assertEqual(on_square(16), 32768)
        assertEqual(total_after(16), 65535)

    ___ test_square_32
        assertEqual(on_square(32), 2147483648)
        assertEqual(total_after(32), 4294967295)

    ___ test_square_64
        assertEqual(on_square(64), 9223372036854775808)
        assertEqual(total_after(64), 18446744073709551615)

    ___ test_square_0_raises_exception
        w__ assertRaises(ValueError):
            on_square(0)
        w__ assertRaises(ValueError):
            total_after(0)

    ___ test_square_negative_raises_exception
        w__ assertRaises(ValueError):
            on_square(-1)
        w__ assertRaises(ValueError):
            total_after(-1)

    ___ test_square_gt_64_raises_exception
        w__ assertRaises(ValueError):
            on_square(65)
        w__ assertRaises(ValueError):
            total_after(65)


__ __name__ __ '__main__':
    unittest.main()
