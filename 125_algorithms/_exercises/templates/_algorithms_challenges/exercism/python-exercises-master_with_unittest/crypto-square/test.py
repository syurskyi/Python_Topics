import unittest

from crypto_square import encode


class CryptoSquareTest(unittest.TestCase):
    ___ test_empty_string(self):
        self.assertEqual(encode(''), '')

    ___ test_perfect_square(self):
        self.assertEqual(encode('ABCD'), 'ac bd')

    ___ test_small_imperfect_square(self):
        self.assertEqual(encode('This is easy!'), 'tis hsy ie sa')

    ___ test_punctuation_and_numbers(self):
        msg = "1, 2, 3, Go! Go, for God's sake!"
        ciph = '1gga 2ook 3fde gos ors'
        self.assertEqual(encode(msg), ciph)

    ___ test_long_string(self):
        msg = ("If man was meant to stay on the ground, god would have given "
               "us roots.")
        ciph = "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"
        self.assertEqual(encode(msg), ciph)


__ __name__ == '__main__':
    unittest.main()
