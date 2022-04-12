# _______ c__
# ____ c.. _______ d.., n..
# _______ __
# ____ u__.r.. _______ u..
#
# BASE_URL 'https://bites-data.s3.us-east-2.amazonaws.com/'
# TMP '/tmp'
#
# fname 'movie_metadata.csv'
# remote __.p...j.. B.. f..
# local __.p...j.. T.. f..
# u.. ? ?
#
# MOVIE_DATA local
# MIN_MOVIES 4
# MIN_YEAR 1960
#
# Movie n.. 'Movie', 'title year score'
#
#
# ___ get_movies_by_director
#     """Extracts all movies from csv and stores them in a dict,
#     where keys are directors, and values are a list of movies,
#     use the defined Movie namedtuple"""
#
#     d d.. l..
#     full_list    # list
#
#     w__ o.. M.. newline='' __ file
#         reader c__.D.. ?
#         ___ row __ reader
#             year row 'title_year'
#             __ ? !_ '' a.. i.. ? > 1960
#                 full_list.a..?  'director_name'
#                                   ?  'movie_title' .s..
#                                   i.. ? 'title_year'
#                                   f__ ? 'imdb_score'
#
#     ___ name movie year score __ f..
#         d name .a.. ? t.._m.. y.._y.. s.._s..
#
#     r.. ?
#
#
# ___ calc_mean_score movies
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     scores movie.s.. ___ ? __ ?
#     r.. r.. s.. ? / l.. ? 1
#
# ___ get_average_scores directors
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#
#     director_list    # list
#     ___ ? __ ?
#         __ l.. ? ? >_ M..
#             d_tuple director c.. ? ?
#             ?.a.. ?
#
#     r.. ?
