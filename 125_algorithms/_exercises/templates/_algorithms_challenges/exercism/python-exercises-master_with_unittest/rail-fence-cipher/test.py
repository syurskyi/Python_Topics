_______ unittest

____ rail_fence_cipher _______ encode, decode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.1

c_ RailFenceTests(unittest.TestCase):
    ___ test_encode_with_two_rails
        assertMultiLineEqual(
            encode('XOXOXOXOXOXOXOXOXO', 2), 'XXXXXXXXXOOOOOOOOO')

    ___ test_encode_with_three_rails
        assertMultiLineEqual(
            encode('WEAREDISCOVEREDFLEEATONCE', 3),
            'WECRLTEERDSOEEFEAOCAIVDEN')

    ___ test_encode_with_ending_in_the_middle
        assertMultiLineEqual(encode('EXERCISES', 4), 'ESXIEECSR')

    ___ test_decode_with_three_rails
        assertMultiLineEqual(
            decode('TEITELHDVLSNHDTISEIIEA', 3), 'THEDEVILISINTHEDETAILS')

    ___ test_decode_with_five_rails
        assertMultiLineEqual(
            decode('EIEXMSMESAORIWSCE', 5), 'EXERCISMISAWESOME')

    ___ test_decode_with_six_rails
        assertMultiLineEqual(
            decode(
                '133714114238148966225439541018335470986172518171757571896261',
                6),
            '112358132134558914423337761098715972584418167651094617711286')


__ __name__ __ '__main__':
    unittest.main()
