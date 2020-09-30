______ unittest

from wordcount ______ word_count


class WordCountTests(unittest.TestCase
    ___ test_count_one_word(self
        self.assertEqual(
            {'word': 1},
            word_count('word')
        )

    ___ test_count_one_of_each(self
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    ___ test_count_multiple_occurences(self
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )

    ___ test_preserves_punctuation(self
        self.assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, ':': 2,
                'javascript!!&@$%^&': 1},
            word_count('car : carpet as java : javascript!!&@$%^&')
        )

    ___ test_include_numbers(self
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    ___ test_mixed_case(self
        self.assertEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            word_count('go Go GO')
        )

    ___ test_multiple_spaces(self
        self.assertEqual(
            {'wait': 1, 'for': 1, 'it': 1}, word_count('wait for       it')
        )

    ___ test_newlines(self
        self.assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
                'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            word_count('rah rah ah ah ah\nroma roma ma\nga ga oh la la\n'
                       'want your bad romance')
        )


__  -n __ '__main__':
    unittest.main()
