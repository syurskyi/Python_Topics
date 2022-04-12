# _______ ___
# _______ __
# _______ j__
#
#
# ___ get_movie_data files l.. __ l..
#     """Parse movie json files into a list of dicts"""
#     out_lst    # list
#     ___ file __ ?
#         w__ o.. ? __ f
#             ?.a.. j__.l.. f
#     ?.s.. key_l.... m ? 'Title'
#     r.. ?
#
#
# ___ get_single_comedy movies l.. __ s..
#     """return the movie with Comedy in Genres"""
#     r.. m ___ ? __ ? __ 'Comedy' __ ? 'Genre' 0 'Title'
#
#
# ___ _get_wins_noms awards s.. __ i..
#     """return the number of wins and noms from award string or 0 if none"""
#     wins __.f.. _([0-9]+)  ?
#     r.. s.. m.. i.. ? __ ? ____ 0
#
#
# ___ get_movie_most_nominations movies l.. __ s..
#     """Return the movie that had the most nominations"""
#     r.. m.. ? key_l.... x _? ? 'Awards'  'Title'
#
#
# ___ _get_runtime runtime s.. __ i..
#     """return the integer runtime from a runtime string"""
#     r.. i.. __.f.. _ ([0-9]+)  ? 0
#
#
# ___ get_movie_longest_runtime movies l.. __ s..
#     """Return the movie that has the longest runtime"""
#     r.. m.. ? key_l.... x _? ? 'Runtime'  'Title'
