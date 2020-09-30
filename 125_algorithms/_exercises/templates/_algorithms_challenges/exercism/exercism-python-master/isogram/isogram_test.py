______ unittest

from isogram ______ is_isogram


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class TestIsogram(unittest.TestCase

    ___ test_empty_string(self
        self.assertIs(is_isogram(""), True)

    ___ test_isogram_with_only_lower_case_characters(self
        self.assertIs(is_isogram("isogram"), True)

    ___ test_word_with_one_duplicated_character(self
        self.assertIs(is_isogram("eleven"), False)

    ___ test_longest_reported_english_isogram(self
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    ___ test_word_with_duplicated_character_in_mixed_case(self
        self.assertIs(is_isogram("Alphabet"), False)

    ___ test_hypothetical_isogrammic_word_with_hyphen(self
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    ___ test_isogram_with_duplicated_hyphen(self
        self.assertIs(is_isogram("six-year-old"), True)

    ___ test_made_up_name_that_is_an_isogram(self
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    ___ test_duplicated_character_in_the_middle(self
        self.assertIs(is_isogram("accentor"), False)

    # # Additional tests for this track

    ___ test_isogram_with_duplicated_letter_and_nonletter_character(self
        self.assertIs(is_isogram("Aleph Bot Chap"), False)


__  -n __ '__main__':
    unittest.main()
