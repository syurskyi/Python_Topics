____ c.. _______ d..

_______ p__

____ directors _______ (get_movies_by_director, get_average_scores,
                       calc_mean_score, Movie)


?p__.f..(scope="module")
___ movies
    r.. get_movies_by_director()


?p__.f..(scope="module")
___ scores(movies
    r.. get_average_scores(movies)


___ test_get_movies_by_director(movies
    ... 'Sergio Leone' __ movies
    ... l..(movies 'Sergio Leone' ) __ 4
    ... l..(movies 'Peter Jackson' ) __ 12


___ test_director_movies_data_structure(movies
    ... t..(movies) __ (d.., d..)
    ... t..(movies 'Peter Jackson' ) __ l..
    ... t..(movies 'Peter Jackson' [0]) __ Movie


___ test_calc_mean_score(movies
    movies_sergio = movies 'Sergio Leone'
    movies_nolan = movies 'Christopher Nolan'
    ... calc_mean_score(movies_sergio) __ 8.5
    ... calc_mean_score(movies_nolan) __ 8.4


___ test_get_average_scores_top_directors(scores
    expected = [('Sergio Leone', 8.5),
                ('Christopher Nolan', 8.4),
                ('Quentin Tarantino', 8.2),
                ('Hayao Miyazaki', 8.2),
                ('Frank Darabont', 8.0),
                ('Stanley Kubrick', 8.0),
                ('James Cameron', 7.9),
                ('Joss Whedon', 7.9)]
    ... scores[0:8] __ expected


?p__.m__.p.("director", [
    'Quentin Tarantino', 'Hayao Miyazaki',
    'Frank Darabont', 'Stanley Kubrick',
    'James Cameron', 'Joss Whedon',
    'Alejandro G. Iñárritu',
])
___ test_director_in_top_scores(director, scores
    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    top_scores = scores[2:13]
    directors = {score[0] ___ score __ top_scores}
    ... director __ directors


___ test_ignore_older_movies(movies
    """Lowell Sherman's Black and White is from 1933 and should
       be skipped"""
    ... l..(movies["Lowell Sherman"]) __ 0