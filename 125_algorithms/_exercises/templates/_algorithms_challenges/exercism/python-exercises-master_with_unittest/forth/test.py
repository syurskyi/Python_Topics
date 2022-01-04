_______ unittest

____ forth _______ evaluate, StackUnderflowError


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0
# Tests for case-insensitivity are track-specific

c_ ForthParsingTest(unittest.TestCase):
    ___ test_numbers_just_get_pushed_to_stack
        input_data = ["1 2 3 4 5"]
        expected = [1, 2, 3, 4, 5]
        assertEqual(evaluate(input_data), expected)


c_ ForthAdditionTest(unittest.TestCase):
    ___ test_can_add_two_numbers
        input_data = ["1 2 +"]
        expected = [3]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["+"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 +"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthSubtractionTest(unittest.TestCase):
    ___ test_can_subtract_two_numbers
        input_data = ["3 4 -"]
        expected = [-1]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["-"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 -"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthMultiplicationTest(unittest.TestCase):
    ___ test_can_multiply_two_numbers
        input_data = ["2 4 *"]
        expected = [8]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["*"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 *"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthDivisionTest(unittest.TestCase):
    ___ test_can_divide_two_numbers
        input_data = ["12 3 /"]
        expected = [4]
        assertEqual(evaluate(input_data), expected)

    ___ test_performs_integer_division
        input_data = ["8 3 /"]
        expected = [2]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_dividing_by_zero
        input_data = ["4 0 /"]
        w__ assertRaisesWithMessage(ZeroDivisionError):
            evaluate(input_data)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["/"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 /"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthCombinedArithmeticTest(unittest.TestCase):
    ___ test_addition_and_subtraction
        input_data = ["1 2 + 4 -"]
        expected = [-1]
        assertEqual(evaluate(input_data), expected)

    ___ test_multiplication_and_division
        input_data = ["2 4 * 3 /"]
        expected = [2]
        assertEqual(evaluate(input_data), expected)


c_ ForthDupTest(unittest.TestCase):
    ___ test_copies_a_value_on_the_stack
        input_data = ["1 dup"]
        expected = [1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_copies_the_top_value_on_the_stack
        input_data = ["1 2 dup"]
        expected = [1, 2, 2]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["dup"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthDropTest(unittest.TestCase):
    ___ test_removes_the_top_value_on_the_stack_if_it_is_the_only_one
        input_data = ["1 DROP"]
        expected    # list
        assertEqual(evaluate(input_data), expected)

    ___ test_removes_the_top_value_on_the_stack_if_it_not_the_only_one
        input_data = ["3 4 DROP"]
        expected = [3]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["drop"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthSwapTest(unittest.TestCase):
    ___ test_swaps_only_two_values_on_stack
        input_data = ["1 2 SWAP"]
        expected = [2, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_swaps_two_two_values_on_stack
        input_data = ["1 2 3 SWAP"]
        expected = [1, 3, 2]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["swap"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 swap"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthOverTest(unittest.TestCase):
    ___ test_copies_the_second_element_if_there_are_only_two
        input_data = ["1 2 OVER"]
        expected = [1, 2, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_copies_the_second_element_if_there_are_more_than_two
        input_data = ["1 2 3 OVER"]
        expected = [1, 2, 3, 2]
        assertEqual(evaluate(input_data), expected)

    ___ test_errors_if_there_is_nothing_on_the_stack
        input_data = ["over"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    ___ test_errors_if_there_is_only_one_value_on_the_stack
        input_data = ["1 over"]
        w__ assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthUserDefinedWordsTest(unittest.TestCase):
    ___ test_can_consist_of_built_in_words
        input_data = [
            ": dup-twice dup dup ;",
            "1 dup-twice"
        ]
        expected = [1, 1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_execute_in_the_right_order
        input_data = [
            ": countup 1 2 3 ;",
            "countup"
        ]
        expected = [1, 2, 3]
        assertEqual(evaluate(input_data), expected)

    ___ test_can_override_other_user_defined_words
        input_data = [
            ": foo dup ;",
            ": foo dup dup ;",
            "1 foo"
        ]
        expected = [1, 1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_can_override_built_in_words
        input_data = [
            ": swap dup ;",
            "1 swap"
        ]
        expected = [1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_can_override_built_in_operators
        input_data = [
            ": + * ;",
            "3 4 +"
        ]
        expected = [12]
        assertEqual(evaluate(input_data), expected)

    ___ test_cannot_redefine_numbers
        input_data = [": 1 2 ;"]
        w__ assertRaisesWithMessage(ValueError):
            evaluate(input_data)

    ___ test_errors_if_executing_a_non_existent_word
        input_data = ["foo"]
        w__ assertRaisesWithMessage(ValueError):
            evaluate(input_data)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


c_ ForthCaseInsensitivityTest(unittest.TestCase):
    ___ test_dup_is_case_insensitive
        input_data = ["1 DUP Dup dup"]
        expected = [1, 1, 1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_drop_is_case_insensitive
        input_data = ["1 2 3 4 DROP Drop drop"]
        expected = [1]
        assertEqual(evaluate(input_data), expected)

    ___ test_swap_is_case_insensitive
        input_data = ["1 2 SWAP 3 Swap 4 swap"]
        expected = [2, 3, 4, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_over_is_case_insensitive
        input_data = ["1 2 OVER Over over"]
        expected = [1, 2, 1, 2, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_user_defined_words_are_case_insensitive
        input_data = [
            ": foo dup ;",
            "1 FOO Foo foo"
        ]
        expected = [1, 1, 1, 1]
        assertEqual(evaluate(input_data), expected)

    ___ test_definitions_are_case_insensitive
        input_data = [
            ": SWAP DUP Dup dup ;",
            "1 swap"
        ]
        expected = [1, 1, 1, 1]
        assertEqual(evaluate(input_data), expected)


__ __name__ __ '__main__':
    unittest.main()
