# -*- coding: utf-8 -*-


_______ unittest

_______ bob


c_ BobTests(unittest.TestCase):

    ___ test_stating_something
        assertEqual(
            'Whatever.',
            bob.hey('Tom-ay-to, tom-aaaah-to.')
        )

    ___ test_shouting
        assertEqual(
            'Whoa, chill out!',
            bob.hey('WATCH OUT!')
        )

    ___ test_asking_a_question
        assertEqual(
            'Sure.',
            bob.hey('Does this cryogenic chamber make me look fat?')
        )

    ___ test_asking_a_numeric_question
        assertEqual(
            'Sure.',
            bob.hey('You are, what, like 15?')
        )

    ___ test_talking_forcefully
        assertEqual(
            'Whatever.',
            bob.hey("Let's go make out behind the gym!")
        )

    ___ test_using_acronyms_in_regular_speech
        assertEqual(
            'Whatever.', bob.hey("It's OK if you don't want to go to the DMV.")
        )

    ___ test_forceful_questions
        assertEqual(
            'Whoa, chill out!', bob.hey('WHAT THE HELL WERE YOU THINKING?')
        )

    ___ test_shouting_numbers
        assertEqual(
            'Whoa, chill out!', bob.hey('1, 2, 3 GO!')
        )

    ___ test_only_numbers
        assertEqual(
            'Whatever.', bob.hey('1, 2, 3')
        )

    ___ test_question_with_only_numbers
        assertEqual(
            'Sure.', bob.hey('4?')
        )

    ___ test_shouting_with_special_characters
        assertEqual(
            'Whoa, chill out!',
            bob.hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
        )

    ___ test_shouting_with_umlauts
        assertEqual(
            'Whoa, chill out!', bob.hey('ÜMLÄÜTS!')
        )

    ___ test_calmly_speaking_with_umlauts
        assertEqual(
            'Whatever.', bob.hey('ÜMLäÜTS!')
        )

    ___ test_shouting_with_no_exclamation_mark
        assertEqual(
            'Whoa, chill out!', bob.hey('I HATE YOU')
        )

    ___ test_statement_containing_question_mark
        assertEqual(
            'Whatever.', bob.hey('Ending with ? means a question.')
        )

    ___ test_prattling_on
        assertEqual(
            'Sure.', bob.hey("Wait! Hang on. Are you going to be OK?")
        )

    ___ test_silence
        assertEqual(
            'Fine. Be that way!', bob.hey('')
        )

    ___ test_prolonged_silence
        assertEqual(
            'Fine. Be that way!', bob.hey('    \t')
        )

    ___ test_starts_with_whitespace
        assertEqual(
            'Whatever.', bob.hey('         hmmmmmmm...')
        )

    ___ test_ends_with_whitespace
        assertEqual(
            'Sure.', bob.hey('What if we end with whitespace?   ')
        )


__ _____ __ _____
    unittest.main()
