# _______ c__
# ____ c.. _______ d.., n..
# _______ __
# ____ u__.r.. _______ u..
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
# Movie n.. 'Movie', 'title year score'
#
#
# ___ get_movies_by_director
#     """Extracts all movies from csv and stores them in a dict,
#     where keys are directors, and values are a list of movies,
#     use the defined Movie namedtuple"""
#
#     movie_metadata d.. l..
#
#     w__ o.. l.. __ file
#         csv_content c__.D.. ?
#
#         ___ row __ ?
#
#             __ ? "title_year" !_ "":
#                 title_year i..? "title_year"
#             ____
#                 _____
#
#             __ title_year > M..
#                 director_name ? "director_name"
#                 movie_title ? "movie_title" .s..
#                 imdb_score f__ ? "imdb_score"
#
#                 __ d.. n.. __ m..
#                     m.. d.. ? m.. t.. i..
#                 ____
#                     m.. d...a.. ? m.. t.. i..
#
#     r.. ?
#
#
# ___ calc_mean_score movies
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     movie_mean movie.s.. ___ ? __ ?
#     r.. r..(s.. ? / l.. ? 1
#
#
# ___ get_average_scores directors
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#     directors_scores    # list
#     ___ key value __ directors.i..
#         director_avg_score c.. ?
#         __ l.. ? >_ M..
#             d__.a.. ? ?
#     r.. s.. ? k.._l.... x| ? 1 r.._T..
#
#
# # if __name__ == "__main__":
# #     test = get_movies_by_director()
# #     print(calc_mean_score(test['Sergio Leone']))
# #     print(get_average_scores(test))