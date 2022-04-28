# ____ c.. _______ n..
#
# MIN_SCORE 4
# DICE_VALUES r.. 1, 7
#
# Player n.. 'Player', 'name scores'
#
#
# ___ calculate_score scores
#     """Based on a list of score ints (dice roll), calculate the
#        total score only taking into account >= MIN_SCORE
#        (= eyes of the dice roll).
#
#        If one of the scores is not a valid dice roll (1-6)
#        raise a ValueError.
#
#        Returns int of the sum of the scores.
#     """
#     ___ score __ ?
#       __ ? n.. __ D..
#         r.. V...
#
#     total_score s.. score ___ ? __ ? __ ? >_ M..
#     r.. ?
#
#
# ___ get_winner players
#     """Given a list of Player namedtuples return the player
#        with the highest score using calculate_score.
#
#        If the length of the scores lists of the players passed in
#        don't match up raise a ValueError.
#
#        Returns a Player namedtuple of the winner.
#        You can assume there is only one winner.
#
#        For example - input:
#          Player(name='player 1', scores=[1, 3, 2, 5])
#          Player(name='player 2', scores=[1, 1, 1, 1])
#          Player(name='player 3', scores=[4, 5, 1, 2])
#
#        output:
#          Player(name='player 3', scores=[4, 5, 1, 2])
#     """
#     previous_player 0
#     ___ i player __ e.. ? start=1
#       __ i __ 1
#         p.. l.. ?.s..
#       ____
#         __ l.. ?.s.. !_ p..
#           r.. V...
#
#     max_score 0
#     max_player ?
#
#     ___ player __ ?
#       current_player_score c.. ?.s..
#       __ ? > m..
#         m.. ?
#         m.. ?
#
#     r.. ?
#
#
# # if __name__ == "__main__":
# #   print(calculate_score([1, 3, 2, 5]))
# #   print(calculate_score([1, 1, 1, 1]))