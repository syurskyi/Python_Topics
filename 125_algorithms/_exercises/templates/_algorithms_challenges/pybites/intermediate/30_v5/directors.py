_______ csv
_______ __
____ c.. _______ d.., n..
____ u__.r.. _______ u..

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = __.p...j..(BASE_URL, fname)
local = __.p...j..(TMP, fname)
u..(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = n..('Movie', 'title year score')


___ get_movies_by_director
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    w__ o.. MOVIE_DATA) __ f:
        reader = csv.DictReader(f)
        films = [{'director': r 'director_name' , 'title': r 'movie_title' , 'year': r 'title_year' ,
                  'score': r 'imdb_score' }
                 ___ r __ reader]
    result = d..()
    ___ r __ films:
        yr = i..(r 'year' , 10) __ r 'year'  ____ 0
        __ yr >= MIN_YEAR:
            score = f__(r 'score' ) __ r 'score'  ____ 0.0
            movie = Movie(r 'title' , yr, score)
            __ r 'director'  __ result:
                result[r 'director']].a..(movie)
            ____
                result[r 'director']] = [movie]
    r.. result


___ calc_mean_score(movies: l..
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    r.. r..(s..(x.score ___ x __ movies) / l..(movies), 1)


___ get_average_scores(directors: d..
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    r.. s..([(d, calc_mean_score(directors[d] ___ d __ directors.k.. __ l..(directors[d]) >= MIN_MOVIES],
                  key=l.... x: -x[1])
