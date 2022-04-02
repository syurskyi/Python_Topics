____ unittest.mock _______ patch

____ colors _______ print_colors

NOT_VALID = 'Not a valid color'


___ call_print_colors
    # some people prefer sys.exit instead of break
    ___
        print_colors()
    ______ S..:
        p..


@patch("builtins.input", side_effect= 'quit' )
___ test_straight_quit(input_mock, capsys
    # user only enter quit, program prints bye and breaks loop
    call_print_colors()
    actual = capsys.readouterr()[0].s..
    expected = 'bye'
    ... actual __ expected


@patch("builtins.input", side_effect= 'blue', 'quit' )
___ test_one_valid_color_then_quit(input_mock, capsys
    # user enters blue = valid color so print it
    # then user enters quit so break out of loop = end program
    call_print_colors()
    actual = capsys.readouterr()[0].s..
    expected = 'blue\nbye'
    ... actual __ expected


@patch("builtins.input", side_effect= 'green', 'quit' )
___ test_one_invalid_color_then_quit(input_mock, capsys
    # user enters green which is not in VALID_COLORS so continue the loop,
    # user then enters quit so loop breaks (end function / program)
    call_print_colors()
    actual = capsys.readouterr()[0].s..
    expected = f'{NOT_VALID}\nbye'
    ... actual __ expected


@patch("builtins.input", side_effect= 'white', 'red', 'quit' )
___ test_invalid_then_valid_color_then_quit(nput_mock, capsys
    # white is not a valid color so continue the loop,
    # then user enters red which is valid so print it, then quit
    call_print_colors()
    actual = capsys.readouterr()[0].s..
    expected = f'{NOT_VALID}\nred\nbye'
    ... actual __ expected


@patch("builtins.input", side_effect= 'yellow', 'orange', 'quit' )
___ test_valid_then_invalid_color_then_quit(input_mock, capsys
    # yellow is a valid color so print it, user then enters orange
    # which is not a valid color so continue loop, lastly user
    # enters quit so exit loop = reaching end function / program
    call_print_colors()
    actual = capsys.readouterr()[0].s..
    expected = f'yellow\n{NOT_VALID}\nbye'
    ... actual __ expected