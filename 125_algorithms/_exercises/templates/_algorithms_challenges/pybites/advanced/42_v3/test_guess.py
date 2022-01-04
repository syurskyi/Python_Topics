____ unittest.mock _______ patch
_______ r__

_______ p__

____ guess _______ get_random_number, Game


@patch.object(r__, 'randint')
___ test_get_random_number(m):
    m.return_value = 17
    ... get_random_number() __ 17


@patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, N..])
___ test_guess(inp):
    game = Game()
    # good
    ... game.guess() __ 11
    ... game.guess() __ 12
    # not a number
    w__ p__.r..(ValueError):
        game.guess()
    # already guessed 12
    w__ p__.r..(ValueError):
        game.guess()
    # good
    ... game.guess() __ 5
    # out of range (x2)
    w__ p__.r..(ValueError):
        game.guess()
    w__ p__.r..(ValueError):
        game.guess()
    # good
    ... game.guess() __ 7
    # hitting enter / no input
    w__ p__.r..(ValueError):
        game.guess()


___ test_validate_guess(capfd):
    """pytest capture stdout:
       https://docs.pytest.org/en/2.9.1/capture.html"""
    game = Game()
    game._answer = 2

    ... n.. game._validate_guess(1)
    out, _ = capfd.readouterr()
    ... out.rstrip() __ '1 is too low'

    ... n.. game._validate_guess(3)
    out, _ = capfd.readouterr()
    ... out.rstrip() __ '3 is too high'

    ... game._validate_guess(2)
    out, _ = capfd.readouterr()
    ... out.rstrip() __ '2 is correct!'


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
___ test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    ... game._win __ T..

    out, _ = capfd.readouterr()
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct!', 'It took you 3 guesses']

    output = [line.s.. ___ line __ out.s..('\n') __ line.s..]
    ___ line, exp __ z..(output, expected):
        ... line __ exp


@patch("builtins.input", side_effect=[N.., 5, 9, 14, 11, 12])
___ test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    ... game._win __ F..

    out, _ = capfd.readouterr()
    expected = ['Please enter a number', '5 is too low',
                '9 is too low', '14 is too high',
                '11 is too low', '12 is too low',
                'Guessed 5 times, answer was 13']

    output = [line.s.. ___ line __ out.s..('\n') __ line.s..]
    ___ line, exp __ z..(output, expected):
        ... line __ exp