_______ unittest

____ scrabble_score _______ score


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ WordTest(unittest.TestCase):
    ___ test_lowercase_letter
        assertEqual(score("a"), 1)

    ___ test_uppercase_letter
        assertEqual(score("A"), 1)

    ___ test_valuable_letter
        assertEqual(score("f"), 4)

    ___ test_short_word
        assertEqual(score("at"), 2)

    ___ test_short_valuable_word
        assertEqual(score("zoo"), 12)

    ___ test_medium_word
        assertEqual(score("street"), 6)

    ___ test_medium_valuable_word
        assertEqual(score("quirky"), 22)

    ___ test_long_mixed_case_word
        assertEqual(score("OxyphenButazone"), 41)

    ___ test_english_like_word
        assertEqual(score("pinata"), 8)

    ___ test_empty_input
        assertEqual(score(""), 0)

    ___ test_entire_alphabet_available
        assertEqual(score("abcdefghijklmnopqrstuvwxyz"), 87)


__ _____ __ _____
    unittest.main()
