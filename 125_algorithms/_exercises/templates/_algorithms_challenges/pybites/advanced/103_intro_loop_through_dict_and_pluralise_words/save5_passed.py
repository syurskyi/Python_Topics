games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

___ print_game_stats(games_won):
    for person, winnings in games_won.items():
        __ winnings >= 2:
            print(f"{person} has won {winnings} games")
        elif winnings == 0: 
            print(f"{person} has won {winnings} games")            
        else:
            print(f"{person} has won {winnings} game")
    pass