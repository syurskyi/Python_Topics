# -*- coding: utf-8 -*-

_______ unittest

____ luhn _______ Luhn


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ LuhnTests(unittest.TestCase):
    ___ test_single_digit_strings_can_not_be_valid
        assertFalse(Luhn("1").is_valid())

    ___ test_a_single_zero_is_invalid
        assertFalse(Luhn("0").is_valid())

    ___ test_a_simple_valid_SIN_that_remains_valid_if_reversed
        assertTrue(Luhn("059").is_valid())

    ___ test_a_simple_valid_SIN_that_becomes_invalid_if_reversed
        assertTrue(Luhn("59").is_valid())

    ___ test_a_valid_Canadian_SIN
        assertTrue(Luhn("055 444 285").is_valid())

    ___ test_invalid_Canadian_SIN
        assertFalse(Luhn("055 444 286").is_valid())

    ___ test_invalid_credit_card
        assertFalse(Luhn("8273 1232 7352 0569").is_valid())

    ___ test_valid_strings_with_a_non_digit_included_become_invalid
        assertFalse(Luhn("055a 444 285").is_valid())

    ___ test_valid_strings_with_punctuation_included_become_invalid
        assertFalse(Luhn("055-444-285").is_valid())

    ___ test_valid_strings_with_symbols_included_become_invalid
        assertFalse(Luhn("055£ 444$ 285").is_valid())

    ___ test_single_zero_with_space_is_invalid
        assertFalse(Luhn("0").is_valid())

    ___ test_more_than_a_single_zero_is_valid
        assertTrue(Luhn("0000 0").is_valid())

    ___ test_input_digit_9_is_correctly_converted_to_output_digit_9
        assertTrue(Luhn("091").is_valid())

    ___ test_is_valid_can_be_called_repeatedly
        # Additional track specific test case
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn("055 444 285")
        assertTrue(number.is_valid())
        assertTrue(number.is_valid())


__ __name__ __ '__main__':
    unittest.main()
