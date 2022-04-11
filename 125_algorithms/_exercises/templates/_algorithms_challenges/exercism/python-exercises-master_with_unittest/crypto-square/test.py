_______ unittest

____ crypto_square _______ encode


c_ CryptoSquareTest(unittest.TestCase
    ___ test_empty_string
        assertEqual(encode(''), '')

    ___ test_perfect_square
        assertEqual(encode('ABCD'), 'ac bd')

    ___ test_small_imperfect_square
        assertEqual(encode('This is easy!'), 'tis hsy ie sa')

    ___ test_punctuation_and_numbers
        msg "1, 2, 3, Go! Go, for God's sake!"
        ciph '1gga 2ook 3fde gos ors'
        assertEqual(encode(msg), ciph)

    ___ test_long_string
        msg ("If man was meant to stay on the ground, god would have given "
               "us roots.")
        ciph "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"
        assertEqual(encode(msg), ciph)


__ _____ __ _____
    unittest.main()
