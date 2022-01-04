_______ unittest

____ phone _______ Phone


c_ PhoneTest(unittest.TestCase):
    ___ test_cleans_number
        number = Phone("(123) 456-7890").number
        assertEqual("1234567890", number)

    ___ test_cleans_number_with_dots
        number = Phone("123.456.7890").number
        assertEqual("1234567890", number)

    ___ test_valid_when_11_digits_and_first_is_1
        number = Phone("11234567890").number
        assertEqual("1234567890", number)

    ___ test_invalid_when_11_digits
        number = Phone("21234567890").number
        assertEqual("0000000000", number)

    ___ test_invalid_when_9_digits
        number = Phone("123456789").number
        assertEqual("0000000000", number)

    ___ test_area_code
        number = Phone("1234567890")
        assertEqual("123", number.area_code())

    ___ test_pretty_print
        number = Phone("1234567890")
        assertEqual("(123) 456-7890", number.pretty())

    ___ test_pretty_print_with_full_us_phone_number
        number = Phone("11234567890")
        assertEqual("(123) 456-7890", number.pretty())


__ _____ __ _____
    unittest.main()
