#     """Loop through games_won's dict (key, value) pairs (dict.items)
#        printing (print, not return) how many games each person has won,
#        pluralize 'game' based on number.
#
#        Expected output (ignore the docstring's indentation):
#
#        sara has won 0 games
#        bob has won 1 game
#        tim has won 5 games
#        julian has won 3 games
#        jim has won 1 game
#
#        (Note that as of Python 3.7 - which we're using atm - dict insert order
#        is retained so no sorting is required for this Bite.)
#     """
#
# games_won  d..(sara0, bob1, tim5, julian3, jim1)
#
# ___ print_game_stats games_won
#     ___ person, winnings __ ?.i..
#         __ ? > 2
#             print_* ? has won ? games
#         ____ w..  0
#             print_* ? has won ? games
#         ____
#             print_* ? has won ? game
#     p..