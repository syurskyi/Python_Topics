_______ unittest

____ rail_fence_cipher _______ encode, decode


c_ RailFenceTests(unittest.TestCase

    ___ test_encode_with_two_rails
        assertMultiLineEqual('XXXXXXXXXOOOOOOOOO',
                                  encode('XOXOXOXOXOXOXOXOXO', 2))

    ___ test_encode_with_three_rails
        assertMultiLineEqual('WECRLTEERDSOEEFEAOCAIVDEN',
                                  encode('WEAREDISCOVEREDFLEEATONCE', 3))

    ___ test_encode_with_middle_stop
        assertMultiLineEqual('ESXIEECSR', encode('EXERCISES', 4))

    ___ test_decode_with_three_rails
        assertMultiLineEqual('THEDEVILISINTHEDETAILS',
                                  d.. 'TEITELHDVLSNHDTISEIIEA', 3))

    ___ test_decode_with_five_rails
        assertMultiLineEqual('EXERCISMISAWESOME',
                                  d.. 'EIEXMSMESAORIWSCE', 5))

    ___ test_decode_with_six_rails
        assertMultiLineEqual(
            '112358132134558914423337761098715972584418167651094617711286',
            d.. '133714114238148966225439541018335470986172518171757571'
                   '896261', 6))


__ _____ __ _____
    unittest.main()
