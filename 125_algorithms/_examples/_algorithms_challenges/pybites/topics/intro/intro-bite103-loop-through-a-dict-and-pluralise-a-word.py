'''
Intro bites
Bite 104 - Split and join

Split up the message on newline (\n) using the split builtin, then use the join builtin to stitch it together using
a '|' (pipe).

So Hello world:\nI am coding in Python :)\nHow awesome! would turn into: Hello world:|I am coding in Python :)|How awesome!

Your code should work for other message strings as well.
'''


games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def my_print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    print(games_won)
    for key, value in games_won.items():
        if value == 1:
            print(f"{key} has won {value} game")
        else:
            print(f"{key} has won {value} games")

    pass

def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for name, num_games in games_won.items():
        games = "game" if num_games == 1 else "games"
        print(f'{name} has won {num_games} {games}')

print_game_stats()