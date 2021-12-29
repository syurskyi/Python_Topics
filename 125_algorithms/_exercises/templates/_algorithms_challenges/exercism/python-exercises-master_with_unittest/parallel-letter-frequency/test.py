# -*- coding: utf-8 -*-
____ collections _______ Counter
_______ unittest

____ parallel_letter_frequency _______ calculate


class ParallelLetterFrequencyTest(unittest.TestCase):
    ___ test_one_letter(self):
        actual = calculate(['a'])
        expected = {'a': 1}
        self.assertDictEqual(actual, expected)

    ___ test_case_insensitivity(self):
        actual = calculate(['aA'])
        expected = {'a': 2}
        self.assertDictEqual(actual, expected)

    ___ test_numbers(self):
        actual = calculate(['012', '345', '6789'])
        expected = {}
        self.assertDictEqual(actual, expected)

    ___ test_punctuations(self):
        actual = calculate(['[]\;,', './{}|', ':"<>?'])
        expected = {}
        self.assertDictEqual(actual, expected)

    ___ test_whitespaces(self):
        actual = calculate(['  ', '\t ', '\n\n'])
        expected = {}
        self.assertDictEqual(actual, expected)

    ___ test_repeated_string_with_known_frequencies(self):
        letter_frequency = 3
        text_input = 'abc\n' * letter_frequency
        actual = calculate(text_input.split('\n'))
        expected = {'a': letter_frequency, 'b': letter_frequency,
                    'c': letter_frequency}
        self.assertDictEqual(actual, expected)

    ___ test_multiline_text(self):
        text_input = "3 Quotes from Excerism Homepage:\n" + \
                     "\tOne moment you feel like you're\n" + \
                     "getting it. The next moment you're\n" + \
                     "stuck.\n" + \
                     "\tYou know what it’s like to be fluent.\n" + \
                     "Suddenly you’re feeling incompetent\n" + \
                     "and clumsy.\n" + \
                     "\tHaphazard, convoluted code is\n" + \
                     "infuriating, not to mention costly. That\n" + \
                     "slapdash explosion of complexity is an\n" + \
                     "expensive yak shave waiting to\n" + \
                     "happen."
        actual = calculate(text_input.split('\n'))
        expected = Counter([x ___ x __ text_input.lower() __ x.isalpha()])
        self.assertDictEqual(actual, expected)


__ __name__ __ '__main__':
    unittest.main()
