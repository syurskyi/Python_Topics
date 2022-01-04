# -*- coding: utf-8 -*-
____ c.. _______ Counter
_______ unittest

____ parallel_letter_frequency _______ calculate


c_ ParallelLetterFrequencyTest(unittest.TestCase):
    ___ test_one_letter
        actual = calculate(['a'])
        expected = {'a': 1}
        assertDictEqual(actual, expected)

    ___ test_case_insensitivity
        actual = calculate(['aA'])
        expected = {'a': 2}
        assertDictEqual(actual, expected)

    ___ test_numbers
        actual = calculate(['012', '345', '6789'])
        expected    # dict
        assertDictEqual(actual, expected)

    ___ test_punctuations
        actual = calculate(['[]\;,', './{}|', ':"<>?'])
        expected    # dict
        assertDictEqual(actual, expected)

    ___ test_whitespaces
        actual = calculate(['  ', '\t ', '\n\n'])
        expected    # dict
        assertDictEqual(actual, expected)

    ___ test_repeated_string_with_known_frequencies
        letter_frequency = 3
        text_input = 'abc\n' * letter_frequency
        actual = calculate(text_input.s..('\n'))
        expected = {'a': letter_frequency, 'b': letter_frequency,
                    'c': letter_frequency}
        assertDictEqual(actual, expected)

    ___ test_multiline_text
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
        actual = calculate(text_input.s..('\n'))
        expected = Counter([x ___ x __ text_input.l.. __ x.isalpha()])
        assertDictEqual(actual, expected)


__ _____ __ _____
    unittest.main()
