_______ unittest

____ word_count _______ word_count


c_ WordCountTests(unittest.TestCase):

    ___ test_count_one_word
        assertEqual(
            {'word': 1},
            word_count('word')
        )

    ___ test_count_one_of_each
        assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    ___ test_count_multiple_occurences
        assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )

    ___ test_ignores_punctuation
        assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1},
            word_count('car : carpet as java : javascript!!&@$%^&')
        )

    ___ test_include_numbers
        assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    ___ test_mixed_case
        assertEqual(
            [2, 3],
            s..(l..(word_count('go Go GO Stop stop').v..
        )

    ___ test_multiple_spaces
        assertEqual(
            {'wait': 1, 'for': 1, 'it': 1},
            word_count('wait for       it')
        )

    ___ test_newlines
        assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            word_count('rah rah ah ah ah\nroma roma ma\n'
                       'ga ga oh la la\nwant your bad romance')
        )

    ___ test_tabs
        assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            word_count('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'
                       'want your bad romance')
        )

    ___ test_non_alphanumeric
        assertEqual(
            {'hey': 1, 'my': 1, 'spacebar': 1, 'is': 1, 'broken': 1},
            word_count('hey,my_spacebar_is_broken.')
        )


__ __name__ __ '__main__':
    unittest.main()
