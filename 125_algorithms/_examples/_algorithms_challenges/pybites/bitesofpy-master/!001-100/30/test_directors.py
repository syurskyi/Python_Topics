from collections import defaultdict
from directors import (get_movies_by_director, get_average_scores,
                       calc_mean_score, Movie)

director_movies = get_movies_by_director()


def test_get_movies_by_director():
    a__ 'Sergio Leone' in director_movies
    a__ len(director_movies['Sergio Leone']) == 4
    a__ len(director_movies['Peter Jackson']) == 12


def test_director_movies_data_structure():
    a__ type(director_movies) in (dict, defaultdict)
    a__ type(director_movies['Peter Jackson']) == list
    a__ type(director_movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies['Sergio Leone']
    movies_nolan = director_movies['Christopher Nolan']
    a__ calc_mean_score(movies_sergio) == 8.5
    a__ calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    # top 2
    scores = get_average_scores(director_movies)

    a__ scores[0] == ('Sergio Leone', 8.5)
    a__ scores[1] == ('Christopher Nolan', 8.4)

    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    directors = {score[0] for score in scores[2:13]}

    a__ 'Quentin Tarantino' in directors
    a__ 'Hayao Miyazaki' in directors
    a__ 'Frank Darabont' in directors
    a__ 'Stanley Kubrick' in directors
    a__ 'James Cameron' in directors
    a__ 'Joss Whedon' in directors
    a__ 'Alejandro G. Iñárritu' in directors