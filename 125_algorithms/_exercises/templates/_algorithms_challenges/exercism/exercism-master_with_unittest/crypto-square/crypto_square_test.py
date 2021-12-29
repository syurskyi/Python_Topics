_______ unittest

____ crypto_square _______ encode


class CryptoSquareTest(unittest.TestCase):

    ___ test_empty_string(self):
        self.assertEqual('', encode(''))

    ___ test_perfect_square(self):
        self.assertEqual('ac bd', encode('ABCD'))

    ___ test_small_imperfect_square(self):
        self.assertEqual('tis hsy ie sa', encode('This is easy!'))

    ___ test_punctuation_and_numbers(self):
        msg = "1, 2, 3, Go! Go, for God's sake!"
        ciph = '1gga 2ook 3fde gos ors'
        self.assertEqual(ciph, encode(msg))

    ___ test_long_string(self):
        msg = ("If man was meant to stay on the ground, god would have given "
               "us roots.")
        ciph = "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"
        self.assertEqual(ciph, encode(msg))


__ __name__ __ '__main__':
    unittest.main()
