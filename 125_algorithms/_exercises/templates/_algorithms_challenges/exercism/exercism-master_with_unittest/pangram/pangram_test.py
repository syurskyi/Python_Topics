# -*- coding: utf-8 -*-

_______ unittest

____ pangram _______ is_pangram


class PangramTests(unittest.TestCase):

    ___ test_empty_string(self):
        self.assertFalse(is_pangram(''))

    ___ test_valid_pangram(self):
        self.assertTrue(
            is_pangram('the quick brown fox jumps over the lazy dog'))

    ___ test_missing_x(self):
        self.assertFalse(is_pangram('a quick movement of the enemy will '
                                    'jeopardize five gunboats'))

    ___ test_mixedcase_and_punctuation(self):
        self.assertTrue(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

    ___ test_unchecked_german_umlaute(self):
        self.assertTrue(is_pangram('Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'))


__ __name__ __ '__main__':
    unittest.main()
