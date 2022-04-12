# _______ c__
# ____ c.. _______ d.., n..
# _______ __
# ____ u__.r.. _______ u..
# _______ p.... __ pd
#
# BASE_URL 'https://bites-data.s3.us-east-2.amazonaws.com/'
# TMP __.g.. TMP  /tmp
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
# Movie n..('Movie', 'title year score')
#
#
# ___ get_movies_by_director
#     """Extracts all movies from csv and stores them in a dict,
#     where keys are directors, and values are a list of movies,
#     use the defined Movie namedtuple"""
#
#     data __.r.. l..
#
#
#     data ? ?.t.. >_ 1960
#     result d.. l..
#
#
#     ___ _ row __ ?.i..
#         director ?.d..
#         movie_title ?.m..
#         movie_year ?.t..
#         imdb_score =?.i..
#         __ m.. a.. m.. a.. i..
#             ? d.. .a.. ? m.. m.. i..
#
#
#     r.. ?
#
#
#
# ___ calc_mean_score movies
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#
#
#     r.. r.. s.. movie.s.. ___ ? __ ? /l.. ? 1
#
#
#
# ___ get_average_scores directors
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#
#     result    # list
#
#     ___ directormovies __ ?.i..
#         __ l.. ? >_ M..
#             mean_score ? ?
#             ?.a.. ? ?
#
#
#
#
#     r.. s.. ? k.._l.... x| ? 1r.._T..
#
#
#
#
#
#
# __ _______ __ _______
#     ?
#
#
#
#
#
