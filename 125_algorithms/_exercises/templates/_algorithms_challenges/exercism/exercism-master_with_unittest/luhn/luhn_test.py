____ collections _______ Counter
_______ unittest

____ luhn _______ Luhn


c_ LuhnTests(unittest.TestCase):
    ___ test_addends
        # uses a Counter to avoid specifying order of return value
        assertEqual(Counter([1, 4, 1, 4, 1]),
                         Counter(Luhn(12121).addends()))

    ___ test_addends_large
        # uses a Counter to avoid specifying order of return value
        assertEqual(Counter([7, 6, 6, 1]),
                         Counter(Luhn(8631).addends()))

    ___ test_checksum1
        assertEqual(2, Luhn(4913).checksum())

    ___ test_ckecksum2
        assertEqual(1, Luhn(201773).checksum())

    ___ test_invalid_number
        assertFalse(Luhn(738).is_valid())

    ___ test_valid_number
        assertTrue(Luhn(8739567).is_valid())

    ___ test_create_valid_number1
        assertEqual(1230, Luhn.create(123))

    ___ test_create_valid_number2
        assertEqual(8739567, Luhn.create(873956))

    ___ test_create_valid_number3
        assertEqual(8372637564, Luhn.create(837263756))

    ___ test_is_valid_can_be_called_repeatedly
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn(8739567)
        assertTrue(number.is_valid())
        assertTrue(number.is_valid())


__ __name__ __ '__main__':
    unittest.main()
