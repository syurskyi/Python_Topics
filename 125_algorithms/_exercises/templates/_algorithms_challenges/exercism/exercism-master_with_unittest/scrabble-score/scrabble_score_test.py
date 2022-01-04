_______ unittest

____ scrabble _______ score


c_ WordTest(unittest.TestCase):
    ___ test_invalid_word_scores_zero
        assertEqual(0, score(''))
        assertEqual(0, score(' \t\n'))
        assertEqual(0, score('hous3'))
        assertEqual(0, score('wo rd'))

    ___ test_scores_very_short_word
        assertEqual(1, score('a'))

    ___ test_scores_other_very_short_word
        assertEqual(4, score('f'))

    ___ test_simple_word_scores_the_number_of_letters
        assertEqual(6, score("street"))

    ___ test_complicated_word_scores_more
        assertEqual(22, score("quirky"))

    ___ test_scores_are_case_insensitive
        assertEqual(41, score("OxyphenButazone"))


__ _____ __ _____
    unittest.main()
