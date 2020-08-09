______ unittest

from bracket_push ______ check_brackets


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

class BracketPushTests(unittest.TestCase
    ___ test_paired_square_brackets(self
        self.assertEqual(check_brackets("[]"), True)

    ___ test_empty_string(self
        self.assertEqual(check_brackets(""), True)

    ___ test_unpaired_brackets(self
        self.assertEqual(check_brackets("[["), False)

    ___ test_wrong_ordered_brackets(self
        self.assertEqual(check_brackets("}{"), False)

    ___ test_wrong_closing_bracket(self
        self.assertEqual(check_brackets("{]"), False)

    ___ test_paired_with_whitespace(self
        self.assertEqual(check_brackets("{ }"), True)

    ___ test_simple_nested_brackets(self
        self.assertEqual(check_brackets("{[]}"), True)

    ___ test_several_paired_brackets(self
        self.assertEqual(check_brackets("{}[]"), True)

    ___ test_paired_and_nested_brackets(self
        self.assertEqual(check_brackets("([{}({}[])])"), True)

    ___ test_unopened_closing_brackets(self
        self.assertEqual(check_brackets("{[)][]}"), False)

    ___ test_unpaired_and_nested_brackets(self
        self.assertEqual(check_brackets("([{])"), False)

    ___ test_paired_and_wrong_nested_brackets(self
        self.assertEqual(check_brackets("[({]})"), False)

    ___ test_math_expression(self
        self.assertEqual(
            check_brackets("(((185 + 223.85) * 15) - 543)/2"), True)

    ___ test_complex_latex_expression(self
        self.assertEqual(
            check_brackets(
                ("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{"
                 "x} &... x^2 \\end{array}\\right)")), True)


__ __name__ __ '__main__':
    unittest.main()
