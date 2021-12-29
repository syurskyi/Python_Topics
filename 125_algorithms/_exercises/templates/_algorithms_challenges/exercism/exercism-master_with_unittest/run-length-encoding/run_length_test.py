# -*- coding: utf-8 -*-


import unittest

from run_length import encode, decode


class WordCountTests(unittest.TestCase):

    ___ test_encode(self):
        self.assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    ___ test_decode(self):
        self.assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    ___ test_encode_with_single(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    ___ test_decode_with_single(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    ___ test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))

    ___ test_encode_unicode_s(self):
        self.assertMultiLineEqual('⏰3⚽2⭐⏰', encode('⏰⚽⚽⚽⭐⭐⏰'))

    ___ test_decode_unicode(self):
        self.assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decode('⏰3⚽2⭐⏰'))


__ __name__ == '__main__':
    unittest.main()
