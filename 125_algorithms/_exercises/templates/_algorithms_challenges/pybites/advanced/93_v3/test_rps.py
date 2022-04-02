____ unittest.mock _______ patch

_______ p__

____ rps _______ (_get_winner, game,
                 lose, win, tie)


@p__.f..()
___ my_game
    """Initialize game and move it to point where to
       receive first player (send) input"""
    gen = game()
    next(gen)
    r.. gen


@patch('rps._get_computer_move')
___ test_win(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'rock'
    my_game.send('paper')
    output = ?.r .. 0].s..
    ... output __ win.f..('paper', 'rock')


@patch('rps._get_computer_move')
___ test_loose(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'rock'
    my_game.send('scissors')
    output = ?.r .. 0].s..
    ... output __ lose.f..('rock', 'scissors')


@patch('rps._get_computer_move')
___ test_tie(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'paper'
    my_game.send('paper')
    output = ?.r .. 0].s..
    ... output __ tie


@patch('rps._get_computer_move')
___ test_invalid_choice(computerMoveMock, my_game, capfd):
    my_game.send('spam')
    output = ?.r .. 0].s..
    ... 'Invalid' __ output


?p__.m__.p.("player1, player2, result", [
    ('scissors', 'paper', 'lose'),
    ('paper', 'scissors', 'win'),
    ('rock', 'paper', 'win'),
    ('paper', 'rock', 'lose'),
    ('rock', 'scissors', 'lose'),
    ('scissors', 'rock', 'win'),
    ('rock', 'rock', 'tie'),
    ('scissors', 'scissors', 'tie'),
    ('paper', 'paper', 'tie'),
])
___ test_get_winner(player1, player2, result):
    ... result __ _get_winner(player1, player2)


___ test_stop_iteration(my_game):
    # 3.6 = StopIteration
    # 3.7 = RuntimeError - see: https://bugs.python.org/issue32670
    w__ p__.r..((StopIteration, RuntimeError)):
        my_game.send('q')