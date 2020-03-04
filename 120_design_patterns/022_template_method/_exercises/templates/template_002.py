# c_ AbstractGame
#      """An abstract class that is common to several games in which
#      players play against the others, but only one is playing at a
#      given time.
#      """
#      ___ - $ $$
#          __  -c __ A..
#              r_ T.. 'abstract class cannot be instantiated'
#
#      ___ playOneGame playersCount
#          ?  ?
#          iG..
#          j _ 0
#          w____ no. eG..
#              mP.. ?
#              ? _ ? + 1 % pC..
#          pW..
#
#      ___ initializeGame
#          r_ T..('abstract method must be overridden')
#
#      ___ endOfGame
#          r_ T..('abstract method must be overridden')
#
#      ___ makePlay player_num
#          r_ T..('abstract method must be overridden')
#
#      ___ printWinner
#          r_ T..('abstract method must be overridden')
#
#
# # Now to create concrete (non-abstract) games, you subclass AbstractGame
# # and override the abstract methods.
#
# c_ Chess A..
#      ___ initializeGame
#          # Put the pieces on the board.
#          p..
#
#      ___ makePlay player
#          # Process a turn for the player
#          p..
#
# # --------- Alex's Martelli example ---------
#
# c_ AbstractBase o..
#     ___ orgMethod
#         ?
#         ?
#
# c_ ConcreteA..
#     ___ doThis
#         p..
#     ___ doThat
#         p..
