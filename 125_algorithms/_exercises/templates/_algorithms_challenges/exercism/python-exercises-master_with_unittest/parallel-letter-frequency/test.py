# -*- coding: utf-8 -*-
____ c.. _______ C..
_______ unittest

____ parallel_letter_frequency _______ calculate


c_ ParallelLetterFrequencyTest(unittest.TestCase
    ___ test_one_letter
        a..  calculate( 'a' )
        e..  {'a': 1}
        assertDictEqual(a.., e..)

    ___ test_case_insensitivity
        a..  calculate( 'aA' )
        e..  {'a': 2}
        assertDictEqual(a.., e..)

    ___ test_numbers
        a..  calculate( '012', '345', '6789' )
        e..    # dict
        assertDictEqual(a.., e..)

    ___ test_punctuations
        a..  calculate( '[]\;,', './{}|', ':"<>?' )
        e..    # dict
        assertDictEqual(a.., e..)

    ___ test_whitespaces
        a..  calculate( '  ', '\t ', '\n\n' )
        e..    # dict
        assertDictEqual(a.., e..)

    ___ test_repeated_string_with_known_frequencies
        letter_frequency  3
        text_input  'abc\n' * letter_frequency
        a..  calculate(text_input.s..('\n'
        e..  {'a': letter_frequency, 'b': letter_frequency,
                    'c': letter_frequency}
        assertDictEqual(a.., e..)

    ___ test_multiline_text
        text_input  "3 Quotes from Excerism Homepage:\n" + \
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
        a..  calculate(text_input.s..('\n'
        e..  C..([x ___ x __ text_input.l.. __ x.i..])
        assertDictEqual(a.., e..)


__ _____ __ _____
    unittest.main()
