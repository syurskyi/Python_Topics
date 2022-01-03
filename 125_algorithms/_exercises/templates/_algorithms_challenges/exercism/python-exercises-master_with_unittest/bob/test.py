_______ unittest

_______ bob


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ BobTests(unittest.TestCase):
    ___ test_stating_something
        assertEqual(bob.hey("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    ___ test_shouting
        assertEqual(bob.hey("WATCH OUT!"), "Whoa, chill out!")

    ___ test_shouting_gibberish
        assertEqual(bob.hey("FCECDFCAAB"), "Whoa, chill out!")

    ___ test_asking_a_question
        assertEqual(
            bob.hey("Does this cryogenic chamber make me look fat?"), "Sure.")

    ___ test_asking_a_numeric_question
        assertEqual(bob.hey("You are, what, like 15?"), "Sure.")

    ___ test_asking_gibberish
        assertEqual(bob.hey("fffbbcbeab?"), "Sure.")

    ___ test_talking_forcefully
        assertEqual(
            bob.hey("Let's go make out behind the gym!"), "Whatever.")

    ___ test_using_acronyms_in_regular_speech
        assertEqual(
            bob.hey("It's OK if you don't want to go to the DMV."),
            "Whatever.")

    ___ test_forceful_question
        assertEqual(
            bob.hey("WHAT THE HELL WERE YOU THINKING?"), "Whoa, chill out!")

    ___ test_shouting_numbers
        assertEqual(bob.hey("1, 2, 3 GO!"), "Whoa, chill out!")

    ___ test_only_numbers
        assertEqual(bob.hey("1, 2, 3"), "Whatever.")

    ___ test_question_with_only_numbers
        assertEqual(bob.hey("4?"), "Sure.")

    ___ test_shouting_with_special_characters
        assertEqual(
            bob.hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!")

    ___ test_shouting_with_no_exclamation_mark
        assertEqual(bob.hey("I HATE YOU"), "Whoa, chill out!")

    ___ test_statement_containing_question_mark
        assertEqual(
            bob.hey("Ending with ? means a question."), "Whatever.")

    ___ test_non_letters_with_question
        assertEqual(bob.hey(":) ?"), "Sure.")

    ___ test_prattling_on
        assertEqual(
            bob.hey("Wait! Hang on. Are you going to be OK?"), "Sure.")

    ___ test_silence
        assertEqual(bob.hey(""), "Fine. Be that way!")

    ___ test_prolonged_silence
        assertEqual(bob.hey("          "), "Fine. Be that way!")

    ___ test_alternate_silence
        assertEqual(bob.hey("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    ___ test_multiple_line_question
        assertEqual(
            bob.hey("\nDoes this cryogenic chamber make me look fat?\nno"),
            "Whatever.")

    ___ test_starting_with_whitespace
        assertEqual(bob.hey("         hmmmmmmm..."), "Whatever.")

    ___ test_ending_with_whitespace
        assertEqual(
            bob.hey("Okay if like my  spacebar  quite a bit?   "), "Sure.")

    ___ test_other_whitespace
        assertEqual(bob.hey("\n\r \t"), "Fine. Be that way!")

    ___ test_non_question_ending_with_whitespace
        assertEqual(
            bob.hey("This is a statement ending with whitespace      "),
            "Whatever.")


__ __name__ __ '__main__':
    unittest.main()
