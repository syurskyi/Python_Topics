from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'

choices = defeated_by.values()

___ _get_computer_move():
    """Randomly select a move"""
    return choice(choices)


___ _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    __ player_choice not in choices:
        return 'Invalid choice'
    __ computer_choice == player_choice:
        return tie
    __ player_choice == defeated_by[computer_choice]:
        return win.format(player_choice, computer_choice)
    else:
        return lose.format(computer_choice,player_choice)


___ game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    while True:
        player_choice = (yield '')
        __ player_choice == 'q':
            raise StopIteration
        computer_choice = _get_computer_move()
        print(_get_winner(computer_choice, player_choice))
