______ unittest

from bracket_push ______ check_brackets


class BracketPushTests(unittest.TestCase

    ___ test_input_empty(self
        self.assertEqual(check_brackets(""), True)

    ___ test_single(self
        self.assertEqual(check_brackets("{}"), True)

    ___ test_unclosed(self
        self.assertEqual(check_brackets("{{"), False)

    ___ test_wrong_order(self
        self.assertEqual(check_brackets("}{"), False)

    ___ test_mixed_not_nested(self
        self.assertEqual(check_brackets("{}[]"), True)

    ___ test_mixed_nested(self
        self.assertEqual(check_brackets("{[]}"), True)

    ___ test_improperly_nested(self
        self.assertEqual(check_brackets("{[}]"), False)

    ___ test_not_opened_nested(self
        self.assertEqual(check_brackets("{[)][]}"), False)

    ___ test_nested_ensemble(self
        self.assertEqual(check_brackets("{[]([()])}"), True)


__  -n __ '__main__':
    unittest.main()
