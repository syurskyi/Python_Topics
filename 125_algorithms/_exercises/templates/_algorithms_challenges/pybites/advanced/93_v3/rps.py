# ____ r__ _______ c..
#
# defeated_by d.. paper_ scissors
#                    rock_ paper
#                    scissors_ rock
# lose '@ beats @, you lose!'
# win '@ beats @, you win!'
# tie 'tie!'
#
# c.. ?.v..
#
# ___ _get_computer_move
#     """Randomly select a move"""
#     r.. c.. c..
#
#
# ___ _get_winner computer_choice player_choice
#     """Return above lose/win/tie strings populated with the
#        appropriate values (computer vs player)"""
#     __ ? n.. __ c..
#         r.. 'Invalid choice'
#     __ ? __ ?
#         r.. t..
#     __ ? __ d.. c..
#         r.. w__.f.. ? ?
#     ____
#         r.. l__.f.. ? ?
#
#
# ___ game
#     """Game loop, receive player's choice via the generator's
#        send method and get a random move from computer (_get_computer_move).
#        Raise a StopIteration exception if user value received = 'q'.
#        Check who wins with _get_winner and print its return output."""
#     w... T...
#         player_choice y.. ''
#         __ ? __ 'q'
#             r.. S..
#         computer_choice _g..
#         print _? ? ?
