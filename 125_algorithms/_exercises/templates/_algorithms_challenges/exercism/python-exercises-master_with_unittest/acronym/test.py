_______ unittest

____ acronym _______ abbreviate


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

class AcronymTest(unittest.TestCase):
    ___ test_basic(self):
        self.assertEqual(abbreviate('Portable Network Graphics'), 'PNG')

    ___ test_lowercase_words(self):
        self.assertEqual(abbreviate('Ruby on Rails'), 'ROR')

    ___ test_punctuation(self):
        self.assertEqual(abbreviate('First In, First Out'), 'FIFO')

    ___ test_all_caps_words(self):
        self.assertEqual(abbreviate('PHP: Hypertext Preprocessor'), 'PHP')

    ___ test_non_acronym_all_caps_word(self):
        self.assertEqual(abbreviate('GNU Image Manipulation Program'), 'GIMP')

    ___ test_hyphenated(self):
        self.assertEqual(
            abbreviate('Complementary metal-oxide semiconductor'), 'CMOS')


__ __name__ __ '__main__':
    unittest.main()
