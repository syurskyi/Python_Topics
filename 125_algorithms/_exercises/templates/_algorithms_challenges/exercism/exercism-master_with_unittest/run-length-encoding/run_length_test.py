# -*- coding: utf-8 -*-


_______ unittest

____ run_length _______ encode, decode


c_ WordCountTests(unittest.TestCase):

    ___ test_encode
        assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    ___ test_decode
        assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    ___ test_encode_with_single
        assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    ___ test_decode_with_single
        assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    ___ test_combination
        assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))

    ___ test_encode_unicode_s
        assertMultiLineEqual('⏰3⚽2⭐⏰', encode('⏰⚽⚽⚽⭐⭐⏰'))

    ___ test_decode_unicode
        assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decode('⏰3⚽2⭐⏰'))


__ _____ __ _____
    unittest.main()
