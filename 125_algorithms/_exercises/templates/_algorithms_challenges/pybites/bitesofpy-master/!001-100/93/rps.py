from random ______ choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'

choices = defeated_by.values()

___ _get_computer_move(
    """Randomly select a move"""
    r_ choice(choices)


___ _get_winner(computer_choice, player_choice
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    __ player_choice not in choices:
        r_ 'Invalid choice'
    __ computer_choice __ player_choice:
        r_ tie
    __ player_choice __ defeated_by[computer_choice]:
        r_ win.format(player_choice, computer_choice)
    ____
        r_ lose.format(computer_choice,player_choice)


___ game(
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    w___ True:
        player_choice = (yield '')
        __ player_choice __ 'q':
            raise StopIteration
        computer_choice = _get_computer_move()
        print(_get_winner(computer_choice, player_choice))
