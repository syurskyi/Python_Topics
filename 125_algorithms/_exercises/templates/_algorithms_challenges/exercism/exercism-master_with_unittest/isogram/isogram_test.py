_______ unittest

____ isogram _______ is_isogram


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

c_ TestIsogram(unittest.TestCase):

    ___ test_empty_string
        assertIs(is_isogram(""), T..)

    ___ test_isogram_with_only_lower_case_characters
        assertIs(is_isogram("isogram"), T..)

    ___ test_word_with_one_duplicated_character
        assertIs(is_isogram("eleven"), F..)

    ___ test_longest_reported_english_isogram
        assertIs(is_isogram("subdermatoglyphic"), T..)

    ___ test_word_with_duplicated_character_in_mixed_case
        assertIs(is_isogram("Alphabet"), F..)

    ___ test_hypothetical_isogrammic_word_with_hyphen
        assertIs(is_isogram("thumbscrew-japingly"), T..)

    ___ test_isogram_with_duplicated_hyphen
        assertIs(is_isogram("six-year-old"), T..)

    ___ test_made_up_name_that_is_an_isogram
        assertIs(is_isogram("Emily Jung Schwartzkopf"), T..)

    ___ test_duplicated_character_in_the_middle
        assertIs(is_isogram("accentor"), F..)

    # Additional tests for this track

    ___ test_isogram_with_duplicated_letter_and_nonletter_character
        assertIs(is_isogram("Aleph Bot Chap"), F..)


__ __name__ __ '__main__':
    unittest.main()
