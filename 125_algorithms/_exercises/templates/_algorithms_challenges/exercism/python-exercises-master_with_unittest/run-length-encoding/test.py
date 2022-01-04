_______ unittest

____ run_length_encoding _______ encode, decode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ WordCountTests(unittest.TestCase):
    ___ test_encode_empty_string
        assertMultiLineEqual(encode(''), '')

    ___ test_encode_single_characters_only_are_encoded_without_count
        assertMultiLineEqual(encode('XYZ'), 'XYZ')

    ___ test_encode_string_with_no_single_characters
        assertMultiLineEqual(encode('AABBBCCCC'), '2A3B4C')

    ___ test_encode_single_characters_mixed_with_repeated_characters
        assertMultiLineEqual(
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
            '12WB12W3B24WB')

    ___ test_encode_multiple_whitespace_mixed_in_string
        assertMultiLineEqual(encode('  hsqq qww  '), '2 hs2q q2w2 ')

    ___ test_encode_lowercase_characters
        assertMultiLineEqual(encode('aabbbcccc'), '2a3b4c')

    ___ test_decode_empty_string
        assertMultiLineEqual(decode(''), '')

    ___ test_decode_single_characters_only
        assertMultiLineEqual(decode('XYZ'), 'XYZ')

    ___ test_decode_string_with_no_single_characters
        assertMultiLineEqual(decode('2A3B4C'), 'AABBBCCCC')

    ___ test_decode_single_characters_with_repeated_characters
        assertMultiLineEqual(
            decode('12WB12W3B24WB'),
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')

    ___ test_decode_multiple_whitespace_mixed_in_string
        assertMultiLineEqual(decode('2 hs2q q2w2 '), '  hsqq qww  ')

    ___ test_decode_lower_case_string
        assertMultiLineEqual(decode('2a3b4c'), 'aabbbcccc')

    ___ test_combination
        assertMultiLineEqual(decode(encode('zzz ZZ  zZ')), 'zzz ZZ  zZ')


__ _____ __ _____
    unittest.main()
