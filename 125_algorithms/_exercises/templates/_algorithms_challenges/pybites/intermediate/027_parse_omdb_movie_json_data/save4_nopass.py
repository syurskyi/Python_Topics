# _______ j__
#
#
# ___ get_movie_data files l.. __ l..
#     """Parse movie json files into a list of dicts"""
#     output    # list
#     ___ movie __ ?
#         ?.a.. d.. j__.l.. o.. ? .r..
#     r.. ?
#
#
# ___ get_single_comedy movies l.. __ s..
#     """return the movie with Comedy in Genres"""
#     r.. movie.g. 'Title' ___ ? __ ? __ 'Comedy' __ ?.g.. 'Genre' 0
#
#
# ___ get_movie_most_nominations movies l.. __ s..
#     """Return the movie that had the most nominations"""
#     output    # list
#     ___ ? __ ?
#         award_count ?.g.. 'Title' i.. ?.g.. 'Awards' .s..  -2
#         ?.a.. ?
#     ?.s.. k.._l.... x ? 1 r.._T..
#     r.. ? 0 0
#
#
# ___ get_movie_longest_runtime movies l.. __ s..
#     """Return the movie that has the longest runtime"""
#     output    # list
#     ___ ? __ ?
#         runtimes ?.g.. 'Title' i.. ?.g.. 'Runtime' .s..  0
#         ?.a.. ?
#     ?.s.. k.._l.... x| ? 1 r.._T..
#     r.. ? 0 0
