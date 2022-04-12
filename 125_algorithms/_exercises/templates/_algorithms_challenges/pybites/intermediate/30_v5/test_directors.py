# ____ c.. _______ d..
# ____ ? _______ g.. g.. c.. M..
#
# director_movies ?
#
#
# ___ test_get_movies_by_director
#     ... 'Sergio Leone' __ ?
#     ... l.. ? 'Sergio Leone'  __ 4
#     ... l.. ? 'Peter Jackson'  __ 12
#
#
# ___ test_director_movies_data_structure
#     ... t.. ? __ d.. d..
#     ... t.. ? 'Peter Jackson'  __ l..
#     ... t.. ? 'Peter Jackson'  0 __ Movie
#
#
# ___ test_calc_mean_score
#     movies_sergio ? 'Sergio Leone'
#     movies_nolan ? 'Christopher Nolan'
#     ... ? ? __ 8.5
#     ... ? ? __ 8.4
#
#
# ___ test_get_average_scores
#     # top 2
#     scores ? ?
#
#     ... ? 0 __ 'Sergio Leone', 8.5
#     ... ? 1 __ 'Christopher Nolan', 8.4
#
#     # order / score might slightly change depending the way the mean
#     # is calculated so only test director names in top scores
#     directors score 0 ___ ? __ ? 2|13
#
#     ... 'Quentin Tarantino' __ ?
#     ... 'Hayao Miyazaki' __ ?
#     ... 'Frank Darabont' __ ?
#     ... 'Stanley Kubrick' __ ?
#     ... 'James Cameron' __ ?
#     ... 'Joss Whedon' __ ?
#     ... 'Alejandro G. Iñárritu' __ ?