_______ p__

____ calculator _______ create_parser, call_calculator


@p__.f..
___ parser
    r.. create_parser()


___ test_one_arg_no_numbers_exits(parser):
    w__ p__.r..(S..):
        args = parser.parse_args(['--add'])
        call_calculator(args=args)


___ test_call_with_wrong_operation(parser):
    w__ p__.r..(S..):
        args = parser.parse_args(['--sum', '10'])
        call_calculator(args=args)


___ test_help_text_hints(parser, capfd):
    w__ p__.r..(S..):
        parser.parse_args(['-h'])

    output = ?.r .. 0].l..
    ... 'usage' __ output
    ... 'a simple calculator' __ output
    ___ op __ 'add sub mul div'.s.. :
        ... op __ output


?p__.m__.p.("args, expected", [
    (['1'], 1),
    (['1', '2'], 3),
    (['1', '2', '3'], 6),
    (['1', '2', '3', '4.5'], 10.5),
])
___ test_add_operations(parser, args, expected):
    args = parser.parse_args(['--add'] + args)
    ... call_calculator(args) __ expected


?p__.m__.p.("args, expected", [
    (['1'], 1),
    (['1', '2'], -1),
    (['10', '7', '0.5'], 2.5),
    (['11', '9', '2.2', '1.8'], -2),
])
___ test_sub_operations(parser, args, expected):
    args = parser.parse_args(['--sub'] + args)
    ... call_calculator(args) __ expected


?p__.m__.p.("args, expected", [
    (['1'], 1),
    (['1', '2'], 2),
    (['3.5', '2', '4.2'], 29.4),
    (['3.5', '2', '4.2', '-1'], -29.4),
])
___ test_mul_operations(parser, args, expected):
    args = parser.parse_args(['--mul'] + args)
    ... call_calculator(args) __ expected


?p__.m__.p.("args, expected", [
    (['2'], 2),
    (['1', '0'], 0),
    (['2.2', '7', '1.1'], 0.29),
    (['3', '2', '3', '5'], 0.1),
])
___ test_div_operations(parser, args, expected):
    args = parser.parse_args(['--div'] + args)
    ... call_calculator(args) __ expected
