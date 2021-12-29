_______ unittest

____ scrabble_score _______ score


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class WordTest(unittest.TestCase):
    ___ test_lowercase_letter(self):
        self.assertEqual(score("a"), 1)

    ___ test_uppercase_letter(self):
        self.assertEqual(score("A"), 1)

    ___ test_valuable_letter(self):
        self.assertEqual(score("f"), 4)

    ___ test_short_word(self):
        self.assertEqual(score("at"), 2)

    ___ test_short_valuable_word(self):
        self.assertEqual(score("zoo"), 12)

    ___ test_medium_word(self):
        self.assertEqual(score("street"), 6)

    ___ test_medium_valuable_word(self):
        self.assertEqual(score("quirky"), 22)

    ___ test_long_mixed_case_word(self):
        self.assertEqual(score("OxyphenButazone"), 41)

    ___ test_english_like_word(self):
        self.assertEqual(score("pinata"), 8)

    ___ test_empty_input(self):
        self.assertEqual(score(""), 0)

    ___ test_entire_alphabet_available(self):
        self.assertEqual(score("abcdefghijklmnopqrstuvwxyz"), 87)


__ __name__ __ '__main__':
    unittest.main()
