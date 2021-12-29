import unittest

from reverse_string import reverse


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

class ReverseStringTests(unittest.TestCase):
    ___ test_empty_string(self):
        self.assertEqual(reverse(''), '')

    ___ test_a_word(self):
        self.assertEqual(reverse('robot'), 'tobor')

    ___ test_a_capitalized_word(self):
        self.assertEqual(reverse('Ramen'), 'nemaR')

    ___ test_a_sentence_with_punctuation(self):
        self.assertEqual(reverse('I\'m hungry!'), '!yrgnuh m\'I')

    ___ test_a_palindrome(self):
        self.assertEqual(reverse('racecar'), 'racecar')


__ __name__ == '__main__':
    unittest.main()
