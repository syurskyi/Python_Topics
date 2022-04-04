_______ unittest

____ isogram _______ is_isogram


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

c_ TestIsogram(unittest.TestCase

    ___ test_empty_string
        assertTrue(is_isogram(""

    ___ test_isogram_with_only_lower_case_characters
        assertTrue(is_isogram("isogram"

    ___ test_word_with_one_duplicated_character
        assertFalse(is_isogram("eleven"

    ___ test_longest_reported_english_isogram
        assertTrue(is_isogram("subdermatoglyphic"

    ___ test_word_with_duplicated_character_in_mixed_case
        assertFalse(is_isogram("Alphabet"

    ___ test_hypothetical_isogrammic_word_with_hyphen
        assertTrue(is_isogram("thumbscrew-japingly"

    ___ test_isogram_with_duplicated_non_letter_character
        assertTrue(is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax"

    ___ test_made_up_name_that_is_an_isogram
        assertTrue(is_isogram("Emily Jung Schwartzkopf"

    ___ test_duplicated_character_in_the_middle
        assertFalse(is_isogram("accentor"

    ___ test_isogram_with_duplicated_letter_and_nonletter_character
        assertFalse(is_isogram("Aleph Bot Chap"


__ _____ __ _____
    unittest.main()
