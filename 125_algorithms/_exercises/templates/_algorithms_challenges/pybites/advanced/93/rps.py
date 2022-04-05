____ r__ _______ c..

defeated_by = d..(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


___ _get_computer_move
    """Randomly select a move"""

    c.. =  'scissors','paper','rock'

    r.. c..(c..)




___ _get_winner(computer_choice, player_choice
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""

     

    computer_defeated_by = defeated_by[computer_choice]
    player_defeated_by = defeated_by[player_choice]

    __ computer_defeated_by __ player_choice:
        r.. win.f..(player_choice,computer_choice)
    ____ player_defeated_by __ computer_choice:
        r.. lose.f..(computer_choice,player_choice)
    ____
        r.. tie










___ game
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    
    


    

    w... T...
        player_choice = y..
        __ player_choice __ 'q':
            r.. S..
        
        __ player_choice n.. __ ('scissors','rock','paper'
            print('Invalid input')
        ____
            computer_choice = _get_computer_move() 
            print(_get_winner(computer_choice,player_choice





