____ winners _______ print_game_stats, games_won


___ test_print_game_stats(capfd):
    winner_prints = ["sara has won 0 games",
                     "bob has won 1 game",
                     "tim has won 5 games",
                     "julian has won 3 games",
                     "jim has won 1 game"]

    print_game_stats(games_won)
    output = ?.r .. 0].splitlines()

    # dict + Python 3.7 = insert order should be retained
    ___ line __ winner_prints:
        ... line __ output