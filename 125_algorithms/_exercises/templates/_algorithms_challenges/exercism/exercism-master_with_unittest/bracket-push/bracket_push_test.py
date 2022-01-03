_______ unittest

____ bracket_push _______ is_paired


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0

c_ BracketPushTest(unittest.TestCase):
    ___ test_paired_square_brackets
        assertEqual(is_paired("[]"), T..)

    ___ test_empty_string
        assertEqual(is_paired(""), T..)

    ___ test_unpaired_brackets
        assertEqual(is_paired("[["), F..)

    ___ test_wrong_ordered_brackets
        assertEqual(is_paired("}{"), F..)

    ___ test_wrong_closing_bracket
        assertEqual(is_paired("{]"), F..)

    ___ test_paired_with_whitespace
        assertEqual(is_paired("{ }"), T..)

    ___ test_partially_paired_brackets
        assertEqual(is_paired("{[])"), F..)

    ___ test_simple_nested_brackets
        assertEqual(is_paired("{[]}"), T..)

    ___ test_several_paired_brackets
        assertEqual(is_paired("{}[]"), T..)

    ___ test_paired_and_nested_brackets
        assertEqual(is_paired("([{}({}[])])"), T..)

    ___ test_unopened_closing_brackets
        assertEqual(is_paired("{[)][]}"), F..)

    ___ test_unpaired_and_nested_brackets
        assertEqual(is_paired("([{])"), F..)

    ___ test_paired_and_wrong_nested_brackets
        assertEqual(is_paired("[({]})"), F..)

    ___ test_paried_and_incomplete_brackets
        assertEqual(is_paired("{}["), F..)

    ___ test_too_many_closing_brackets
        assertEqual(is_paired('[]]'), F..)

    ___ test_math_expression
        assertEqual(
            is_paired("(((185 + 223.85) * 15) - 543)/2"), T..)

    ___ test_complex_latex_expression
        assertEqual(
            is_paired(
                ("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{"
                 "x} &... x^2 \\end{array}\\right)")), T..)


__ __name__ __ '__main__':
    unittest.main()
