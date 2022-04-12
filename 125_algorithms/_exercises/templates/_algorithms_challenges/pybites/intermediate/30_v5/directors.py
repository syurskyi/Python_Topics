# _______ c__
# _______ __
# ____ c.. _______ d.., n..
# ____ u__.r.. _______ u..
#
# BASE_URL 'http://projects.bobbelderbos.com/pcc/movies/'
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
#     w__ o.. M.. __ f
#         reader c__.D.. ?
#         films 'director': r 'director_name' , 'title': r 'movie_title' , 'year': r 'title_year' ,
#                   'score': r 'imdb_score'
#                  ___ r __ r..
#     result d..
#     ___ r __ ?
#         yr i.. ? 'year'  10 __ ? 'year'  ____ 0
#         __ yr >_ M..
#             score f__ ? 'score'  __ ? 'score'  ____ 0.0
#             movie ? ? 'title' ? ?
#             __ ? 'director'  __ ?
#                 ? ? 'director' .a.. ?
#             ____
#                 ? ? 'director' ?
#     r.. ?
#
#
# ___ calc_mean_score movies l..
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     r.. r.. s.. x.s.. ___ ? __ ? / l.. ? 1
#
#
# ___ get_average_scores directors d..
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#     r.. s.. d ? ? ? ___ d __ ?.k.. __ l.. ? ? >_ M.. k.._l.... x| -? 1
