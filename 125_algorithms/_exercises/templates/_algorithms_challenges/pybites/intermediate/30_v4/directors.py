# _______ c__
# ____ c.. _______ d.., n..
# _______ __
# ____ u__.r.. _______ u..
#
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
# # field conversion
# fields   'movie_title', 'title_year', 'imdb_score'
# conv s.. i.. f__
# NAME 'director_name'
#
#
# ___ get_movies_by_director
#     """Extracts all movies from csv and stores them in a dict,
#     where keys are directors, and values are a list of movies,
#     use the defined Movie namedtuple"""
#     movie_dict d.. l..
#     reader c__.D.. o.. l..
#
#     ___ row __ ?
#         __ ? 'title_year'
#             __ i.. ? 'title_year' .s.. < 1960
#                 _____
#         ____
#             _____
#         remap fun ? x ___ ? ? __ z.. c.. f..
#         m.. ? N__ .a.. ? $?
#     r.. ?
#
#
# ___ calc_mean_score movies
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     __ ?
#         avg r.. s.. m.s.. ___ ? __ ? /l.. ? 1
#     ____
#         avg 0
#     r.. ?
#
#
# ___ get_average_scores directors
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#
#     r.. s.. d, c.. m
#                    ___ ? ? __ ?.i.. __ l.. ? >_ M.. r.._T.. k.._l.... x| ? 1
