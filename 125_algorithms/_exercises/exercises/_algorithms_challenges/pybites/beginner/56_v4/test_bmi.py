# _______ p__
#
# ____ Previous.bmi _______ create_parser, handle_args
#
#
# @p__.f..
# ___ parser
#     r.. ?
#
#
# ___ test_no_args_exits parser
#     # parser.parse_args should raise the exception but in case
#     # you raised it explicitly further down the stack let's check
#     # if handle_args raises it (same applies to next test)
#     w__ p__.r.. S..
#         ?
#
#
# ___ test_help_flag_exits parser
#     w__ p__.r.. S..
#         args  ?.p.. h'
#         ? ?
#
#
# ___ test_only_width_exits parser
#     w__ p__.r.. S..
#         args  ?.p.. '-w', '80'
#         ? ?
#
#
# ___ test_only_length_exits parser
#     w__ p__.r.. S..
#         args  ?.p.. '-l', '187'
#         ? ?
#
#
# ___ test_two_arg parser capfd
#     args ?.p.. '-w', '80', '-l', '187'
#     ? ?
#     output  ?.r .. 0
#     ... "Your BMI is: 22.88" __ ?
#
#
# ___ test_two_arg_reversed_order parser, capfd
#     args ?.p.. '-l', '187', '-w', '80'
#     ? ?
#     output  ?.r .. 0
#     ... "Your BMI is: 22.88" __ ?
#
#
# ___ test_different_args parser capfd
#     args  ?.p.. '-l', '200', '-w', '100'
#     ? ?
#     output  ?.r .. 0
#     ... "Your BMI is: 25.0" __ ?