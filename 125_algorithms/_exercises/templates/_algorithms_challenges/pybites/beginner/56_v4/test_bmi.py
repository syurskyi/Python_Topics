_______ p__

____ Previous.bmi _______ create_parser, handle_args


@p__.fixture
___ parser
    r.. create_parser()


___ test_no_args_exits(parser):
    # parser.parse_args should raise the exception but in case
    # you raised it explicitly further down the stack let's check
    # if handle_args raises it (same applies to next test)
    w__ p__.r..(SystemExit):
        handle_args()


___ test_help_flag_exits(parser):
    w__ p__.r..(SystemExit):
        args = parser.parse_args(['-h'])
        handle_args(args)


___ test_only_width_exits(parser):
    w__ p__.r..(SystemExit):
        args = parser.parse_args(['-w', '80'])
        handle_args(args)


___ test_only_length_exits(parser):
    w__ p__.r..(SystemExit):
        args = parser.parse_args(['-l', '187'])
        handle_args(args)


___ test_two_arg(parser, capfd):
    args = parser.parse_args(['-w', '80', '-l', '187'])
    handle_args(args)
    output = capfd.readouterr()[0]
    ... "Your BMI is: 22.88" __ output


___ test_two_arg_reversed_order(parser, capfd):
    args = parser.parse_args(['-l', '187', '-w', '80'])
    handle_args(args)
    output = capfd.readouterr()[0]
    ... "Your BMI is: 22.88" __ output


___ test_different_args(parser, capfd):
    args = parser.parse_args(['-l', '200', '-w', '100'])
    handle_args(args)
    output = capfd.readouterr()[0]
    ... "Your BMI is: 25.0" __ output