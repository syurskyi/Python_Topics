____ c.. _______ d..
____ directors _______ (get_movies_by_director, get_average_scores,
                       calc_mean_score, Movie)

director_movies = get_movies_by_director()


___ test_get_movies_by_director
    ... 'Sergio Leone' __ director_movies
    ... l..(director_movies 'Sergio Leone' ) __ 4
    ... l..(director_movies 'Peter Jackson' ) __ 12


___ test_director_movies_data_structure
    ... t..(director_movies) __ (d.., d..)
    ... t..(director_movies 'Peter Jackson' ) __ l..
    ... t..(director_movies 'Peter Jackson' [0]) __ Movie


___ test_calc_mean_score
    movies_sergio = director_movies 'Sergio Leone'
    movies_nolan = director_movies 'Christopher Nolan'
    ... calc_mean_score(movies_sergio) __ 8.5
    ... calc_mean_score(movies_nolan) __ 8.4


___ test_get_average_scores
    # top 2
    scores = get_average_scores(director_movies)

    ... scores[0] __ ('Sergio Leone', 8.5)
    ... scores[1] __ ('Christopher Nolan', 8.4)

    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    directors = {score[0] ___ score __ scores[2:13]}

    ... 'Quentin Tarantino' __ directors
    ... 'Hayao Miyazaki' __ directors
    ... 'Frank Darabont' __ directors
    ... 'Stanley Kubrick' __ directors
    ... 'James Cameron' __ directors
    ... 'Joss Whedon' __ directors
    ... 'Alejandro G. Iñárritu' __ directors