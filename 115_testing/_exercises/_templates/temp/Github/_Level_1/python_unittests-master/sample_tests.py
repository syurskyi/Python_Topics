# ______ pytest
# ______ sample_functions
#
#
# ___ test_sum(
#     num1 _ 5
#     num2 _ 10
#     expected _ 15
#     a.. sample_functions.sum(num1, num2) __ 15
#
# ___ test_contains_numbers(
#     input_str _ "el12lk3j5mnfadf"
#     a.. sample_functions.contains_numbers(input_str) __ T..
#
# ___ test_does_not_contain_numbers(
#     input_str _ "lkqwjqlkjlkjed"
#     a.. sample_functions.contains_numbers(input_str) __ F..
#
# ___ test_div(
#     num1 _ 10
#     num2 _ 5
#     expected _ 2
#     a.. sample_functions.div(num1, num2) __ expected
#
# ___ test_div_by_zero(
#     num1 _ 10
#     num2 _ 0
#     w__ pytest.raises(Z..
#         sample_functions.div(num1, num2)
#
#
# #Create separate and independent test cases
# #For instance, avoid this:
# ___ test_div2(
#     num1 _ 10
#     num2 _ 5
#     expected _ 2
#     a.. sample_functions.div(num1, num2) __ expected
#     num2 _ 0
#     w__ pytest.raises(Z..
#         sample_functions.div(num1, num2)
# #Two aspects being tested under the same test case. Not a good practice.