    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game

       (Note that as of Python 3.7 - which we're using atm - dict insert order
       is retained so no sorting is required for this Bite.)
    """

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

___ print_game_stats(games_won):
    for person, winnings in games_won.items():
        __ winnings >= 2:
            print(f"{person} has won {winnings} games")
        elif winnings = 0: 
            print(f"{person} has won {winnings} games")            
        else:
            print(f"{person} has won {winnings} game")
    pass