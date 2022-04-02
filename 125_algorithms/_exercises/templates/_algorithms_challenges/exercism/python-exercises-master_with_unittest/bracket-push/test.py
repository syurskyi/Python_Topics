_______ unittest

____ bracket_push _______ check_brackets


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

c_ BracketPushTests(unittest.TestCase
    ___ test_paired_square_brackets
        assertEqual(check_brackets("[]"), T..)

    ___ test_empty_string
        assertEqual(check_brackets(""), T..)

    ___ test_unpaired_brackets
        assertEqual(check_brackets("[["), F..)

    ___ test_wrong_ordered_brackets
        assertEqual(check_brackets("}{"), F..)

    ___ test_wrong_closing_bracket
        assertEqual(check_brackets("{]"), F..)

    ___ test_paired_with_whitespace
        assertEqual(check_brackets("{ }"), T..)

    ___ test_simple_nested_brackets
        assertEqual(check_brackets("{[]}"), T..)

    ___ test_several_paired_brackets
        assertEqual(check_brackets("{}[]"), T..)

    ___ test_paired_and_nested_brackets
        assertEqual(check_brackets("([{}({}[])])"), T..)

    ___ test_unopened_closing_brackets
        assertEqual(check_brackets("{[)][]}"), F..)

    ___ test_unpaired_and_nested_brackets
        assertEqual(check_brackets("([{])"), F..)

    ___ test_paired_and_wrong_nested_brackets
        assertEqual(check_brackets("[({]})"), F..)

    ___ test_math_expression
        assertEqual(
            check_brackets("(((185 + 223.85) * 15) - 543)/2"), T..)

    ___ test_complex_latex_expression
        assertEqual(
            check_brackets(
                ("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{"
                 "x} &... x^2 \\end{array}\\right)")), T..)


__ _____ __ _____
    unittest.main()
