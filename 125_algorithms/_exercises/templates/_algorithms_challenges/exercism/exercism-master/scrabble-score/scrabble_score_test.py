______ unittest

from scrabble ______ score


class WordTest(unittest.TestCase
    ___ test_invalid_word_scores_zero(self
        self.assertEqual(0, score(''))
        self.assertEqual(0, score(' \t\n'))
        self.assertEqual(0, score('hous3'))
        self.assertEqual(0, score('wo rd'))

    ___ test_scores_very_short_word(self
        self.assertEqual(1, score('a'))

    ___ test_scores_other_very_short_word(self
        self.assertEqual(4, score('f'))

    ___ test_simple_word_scores_the_number_of_letters(self
        self.assertEqual(6, score("street"))

    ___ test_complicated_word_scores_more(self
        self.assertEqual(22, score("quirky"))

    ___ test_scores_are_case_insensitive(self
        self.assertEqual(41, score("OxyphenButazone"))


__ __name__ __ '__main__':
    unittest.main()
