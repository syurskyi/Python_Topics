_______ unittest

____ acronym _______ abbreviate


c_ AcronymTest(unittest.TestCase):

    ___ test_basic
        assertEqual('PNG', abbreviate('Portable Network Graphics'))

    ___ test_lowercase_words
        assertEqual('ROR', abbreviate('Ruby on Rails'))

    ___ test_camelcase
        assertEqual('HTML', abbreviate('HyperText Markup Language'))

    ___ test_punctuation
        assertEqual('FIFO', abbreviate('First In, First Out'))

    ___ test_all_caps_words
        assertEqual('PHP', abbreviate('PHP: Hypertext Preprocessor'))

    ___ test_hyphenated
        assertEqual('CMOS',
                         abbreviate('Complementary metal-oxide semiconductor'))


__ __name__ __ '__main__':
    unittest.main()
