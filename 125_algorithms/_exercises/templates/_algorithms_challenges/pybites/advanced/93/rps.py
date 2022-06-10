# ____ r__ _______ c..
#
# defeated_by d.. paper_ scissors
#                    rock_ paper
#                    scissors_ rock
# lose '@ beats @, you lose!'
# win '{} beats {}, you win!'
# tie 'tie!'
#
#
# ___ _get_computer_move
#     """Randomly select a move"""
#
#     c.. =  'scissors','paper','rock'
#
#     r.. c.. c..
#
#
#
#
# ___ _get_winner computer_choice player_choice
#     """Return above lose/win/tie strings populated with the
#        appropriate values (computer vs player)"""
#
#
#
#     computer_defeated_by d.. ?
#     player_defeated_by d.. ?
#
#     __ c.. __ ?
#         r.. w__.f.. ? ?
#     ____ p.. __ c..
#         r.. l__.f.. ? ?
#     ____
#         r.. ?
#
#
# ___ game
#     """Game loop, receive player's choice via the generator's
#        send method and get a random move from computer (_get_computer_move).
#        Raise a StopIteration exception if user value received = 'q'.
#        Check who wins with _get_winner and print its return output."""
#
#
#
#
#
#
#     w... T...
#         player_choice y..
#         __ ? __ 'q'
#             r.. S..
#
#         __ ? n.. __ ('scissors','rock','paper'
#             print('Invalid input')
#         ____
#             computer_choice _?
#             print _? ? ?
#
#
#
#
#
