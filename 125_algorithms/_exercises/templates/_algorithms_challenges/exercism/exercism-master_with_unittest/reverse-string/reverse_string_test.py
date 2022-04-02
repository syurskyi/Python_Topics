_______ unittest

____ reverse_string _______ reverse


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

c_ ReverseStringTests(unittest.TestCase
    ___ test_empty_string
        assertEqual(reverse(''), '')

    ___ test_a_word
        assertEqual(reverse('robot'), 'tobor')

    ___ test_a_capitalized_word
        assertEqual(reverse('Ramen'), 'nemaR')

    ___ test_a_sentence_with_punctuation
        assertEqual(reverse('I\'m hungry!'), '!yrgnuh m\'I')

    ___ test_a_palindrome
        assertEqual(reverse('racecar'), 'racecar')


__ _____ __ _____
    unittest.main()
