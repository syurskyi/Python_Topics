______ unittest

from pangram ______ is_pangram


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class PangramTests(unittest.TestCase
    ___ test_sentence_empty(self
        self.assertFalse(is_pangram(''))

    ___ test_pangram_with_only_lower_case(self
        self.assertTrue(
            is_pangram('the quick brown fox jumps over the lazy dog'))

    ___ test_missing_character_x(self
        self.assertFalse(
            is_pangram('a quick movement of the enemy will '
                       'jeopardize five gunboats'))

    ___ test_another_missing_character_x(self
        self.assertFalse(
            is_pangram('the quick brown fish jumps over the lazy dog'))

    ___ test_pangram_with_underscores(self
        self.assertTrue(
            is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'))

    ___ test_pangram_with_numbers(self
        self.assertTrue(
            is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs'))

    ___ test_missing_letters_replaced_by_numbers(self
        self.assertFalse(
            is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'))

    ___ test_pangram_with_mixedcase_and_punctuation(self
        self.assertTrue(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

    ___ test_upper_and_lower_case_versions_of_the_same_character(self
        self.assertFalse(
            is_pangram('the quick brown fox jumped over the lazy FOX'))


__ __name__ __ '__main__':
    unittest.main()
