'''
Intro bites
Bite 104 - Split and join

Split up the message on newline (\n) using the split builtin, then use the join builtin to stitch it together using
a '|' (pipe).

So Hello world:\nI am coding in Python :)\nHow awesome! would turn into: Hello world:|I am coding in Python :)|How awesome!

Your code should work for other message strings as well.
'''


games_won = d..(sara=0, bob=1, tim=5, julian=3, jim=1)


___ my_print_game_stats(games_won=games_won
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    print(games_won)
    ___ key, value __ games_won.i..:
        __ value __ 1:
            print(f"{key} has won {value} game")
        ____
            print(f"{key} has won {value} games")

    p..

___ print_game_stats(games_won=games_won
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    ___ name, num_games __ games_won.i..:
        games = "game" __ num_games __ 1 ____ "games"
        print _*{name} has won {num_games} {games}')

print_game_stats()