_______ unittest

____ acronym _______ abbreviate


class AcronymTest(unittest.TestCase):

    ___ test_basic(self):
        self.assertEqual('PNG', abbreviate('Portable Network Graphics'))

    ___ test_lowercase_words(self):
        self.assertEqual('ROR', abbreviate('Ruby on Rails'))

    ___ test_camelcase(self):
        self.assertEqual('HTML', abbreviate('HyperText Markup Language'))

    ___ test_punctuation(self):
        self.assertEqual('FIFO', abbreviate('First In, First Out'))

    ___ test_all_caps_words(self):
        self.assertEqual('PHP', abbreviate('PHP: Hypertext Preprocessor'))

    ___ test_hyphenated(self):
        self.assertEqual('CMOS',
                         abbreviate('Complementary metal-oxide semiconductor'))


__ __name__ __ '__main__':
    unittest.main()
